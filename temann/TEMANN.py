from keras.models import model_from_json
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder

from temann import DataSet
from temann.data import TEMDB
from temann.querry import *
from temann.spacegroup import *
from temann.util import *


class TEMANN:
    
    def __init__(self):
        self.scaler = None
        self.model = None
        self.encoder = {}
        return
    
    def load_model(self, json_file, weights_file):
        """
        Loads and compiles the trained neural network from 
        the serialized json file and a weights file.

        Input:
        json_file, (string)
        weights_file, (string)

        Output:
        loaded_model, (keras.model)
        """

        json_model = open(json_file, 'r')
        loaded_model_json = json_model.read()
        json_model.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(weights_file)
        loaded_model.compile(loss='mean_squared_error', optimizer='Adadelta')
        self.model = loaded_model
        return
    
    def load_scaler(self, scaler_file):
        """
        Loads the scaler used when training the model.
        """
        self.scaler = joblib.load(file_path(scaler_file))
        return

    def load_encoder(self, encoder_file, encoder_id):
        self.encoder[encoder_id] = joblib.load(file_path(encoder_file))
        return

    def _encode_categorical(self, feature, encoder_id):
        return int(self.encoder[encoder_id].transform([feature]))
    
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
    
    def _transform_spacegroup(self, spacegroup):
        """
        Input:
        spacegroup, (int)

        Output:
        encoded categorical spacegroup features (np.array)
        """
        sg_features = list(expand_spacegroup(spacegroup))
        for i in range(1, 3):
            sg_features[i] = self._encode_categorical(sg_features[i], i-1)
        return np.array(sg_features)
    
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
        #scaled_features.reshape((1, -1))
        return scaled_features

    def predict(self, compound, spacegroup, T):
        prediction = self.model.predict(self._transform_input(compound,
                                                        spacegroup, T))
        return float(prediction)
