from keras.models import model_from_json
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder

from temann import DataSet
from temann.querry import *
from temann.spacegroup import *
from temann.util import *


class TEMANN:
    
    def __init__(self):
        self.scaler = None
        self.model = None
        self.encoder = {}
        
        return

    def load_model(self):
        self._load_scaler('scaler.save')
        self._load_encoder('encoder0.save', 0)
        self._load_encoder('encoder1.save', 1)
        self._load_model('model.json', 'model.h5')
        return
    
    def _load_model(self, json_file, weights_file):
        """
        Loads and compiles the trained neural network from 
        the serialized json file and a weights file.

        Input:
        json_file, (string)
        weights_file, (string)

        Output:
        loaded_model, (keras.model)
        """

        json_model = open(file_path(json_file), 'r')
        loaded_model_json = json_model.read()
        json_model.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(file_path(weights_file))
        loaded_model.compile(loss='mean_squared_error', optimizer='Adadelta')
        self.model = loaded_model
        return
    
    def _load_scaler(self, scaler_file):
        """
        Loads the scaler used when training the model.
        """
        self.scaler = joblib.load(file_path(scaler_file))
        return

    def _load_encoder(self, encoder_file, encoder_id):
        """
        """
        loaded_encoder = joblib.load(file_path(encoder_file))
        encoder_dict = {}
        for cl in loaded_encoder.classes_:
            encoder_dict[cl] = [float(x) for x in
                   cl == loaded_encoder.classes_]
        self.encoder[encoder_id] = encoder_dict
        return

    def _expand_channels(self, i, original, to_be_inserted):
        del original[i]
        to_be_inserted.reverse()
        for value in to_be_inserted:
            original.insert(i, value)
        return original
    
    def _transform_spacegroup(self, spacegroup):
        """
        Input:
        spacegroup, (int)

        Output:
        encoded categorical spacegroup features (np.array)
        """
        sg_features = list(expand_spacegroup(spacegroup))
        for i in np.arange(2, 0, -1):
            extra_channels = self.encoder[i-1][sg_features[i]]
            sg_features = self._expand_channels(i, sg_features, extra_channels)
#            del sg_features[i]
#            extra_channels.reverse()
#            for value in extra_channels:
#                sg_features.insert(i,value)
            
        return np.array(sg_features)
    
    def _transform_compound(self, compound):
        """
        Converts one sample to raw data for predicting thru ANN.
        """
        cmpd_features = np.array(compound_short_descriptors(compound),
                                 dtype=np.float)
        cmpd_features = np.pad(cmpd_features, (0, 80-cmpd_features.shape[0]),
                               mode='constant')
        cmpd_features = np.nan_to_num(cmpd_features)
        
        return cmpd_features
    
    def _join_features(self, cmpd_features, sg_features, T):
        """
        Input:
        compound and spacegroup feature vectors

        Output:
        joined
        """
        return np.concatenate((cmpd_features, [T], sg_features))
    
    def _scale_features(self, features):
        return self.scaler.transform(features.reshape(1, -1))
    
    def _transform_input(self, compound, spacegroup, T):
        cmpd_features = self._transform_compound(compound)
        sg_features = self._transform_spacegroup(spacegroup)
        joined_features = self._join_features(cmpd_features, sg_features, T)
        scaled_features = self._scale_features(joined_features)
        return scaled_features

    def predict(self, compound, spacegroup, T):
        prediction = self.model.predict(self._transform_input(compound,
                                                        spacegroup, T))
        return float(prediction)
