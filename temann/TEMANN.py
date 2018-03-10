# imports here

def encode_categorical(feature):
    
    return encoded_feature


class TEMANN:
    
    def __init__(self):
        self.scaler = None
        self.model = None
        self.encoder = None
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
    
    def load_encoder(self, encoder_file):
        self.encoder = joblib.load(file_path(encoder_file))
        return
    
    def _transform_compound(self, compound):
        """Converts one sample to raw data for predicting thru ANN"""
        array = np.zeros(80) # create an empty array with zeros
        descriptors = np.array(compound_short_descriptors(compound)) # load descriptors 
        for index, x in np.ndenumerate(descriptors):
            array[index] = x
        ndf = pd.DataFrame(data=array)
        # clean up the data (get rid of strings and NaNs.)
        ndf = ndf.append([T])
        ndf.apply(pd.to_numeric)
        ndf = ndf.fillna(0)

#         array = self.scaler.transform(ndf)
#         array = array.T
        return ndf
    
    def _transform_spacegroup(self, spacegroup):
        """
        Input:
        spacegroup, (int)

        Output:
        encoded categorical spacegroup features

        uses encode_categorical()
        """
        return spacegroup_features
    
    def _join_features(self, compound_features, spacegroup_features, T):
        """
        Input:
        compound and spacegroup feature vectors

        Output:
        joined
        """

        return joined_features
    
    def _scale_features(self, features):
        return self.scaler.transform(scaled_features)
    
    def _transform_input():
        return features
    
    def predict(self, compound, spacegroup, T):
        return self.model.predict(self._transform_input(compound, spacegroup, T))
