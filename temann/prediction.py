from keras.models import model_from_json
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

from .DataSet import DataSet
from .interpret import *
from .querry import *
from .spacegroup import *
from .util import *


__all__ = ['predict_seebeck', 'TEMANN']


class TEMANN:
    """
    Loads in the saved model and predicts Seebeck coefficients.

    Attributes:
        scaler (sklearn.preprocessing.data.StandardScaler): Scaler used
            for the training set.
        encoder (dict of dict): Dictionary containing 2 dictionaries.
            Each sub-dictionary is used to split the single channel
            categorical value into multiple channels of binary values.
        model (keras.models.Sequential): Contains the trained
            artificial neural network.
    """

    def __init__(self):
        """
        Loads all attributes with the _load_model() method.
        """
        self.scaler = None
        self.model = None
        self.encoder = {}

        self._load_model()
        return

    def predict(self, compound, spacegroup, T):
        """
        Uses a trained neural network to predict Seebeck coefficient.

        Args:
            compound (str): Chemical formula of material of interest.
            spacegroup (int or float): Space group number of material of
                interest.
            T (int or float): Temperature of interest.

        Returns:
            float: Predicted Seebeck coefficient.

        Raises:
            TypeError: If `compound` is not a string.
            TypeError: If `spacegroup` is not an int or float.
            TypeError: If `T` is not an int or float.
            Exception: If `compound` contains more than 5
                unique elements.
        """

        prediction = self.model.predict(self._transform_input(compound,
                                                              spacegroup, T))
        return float(prediction)

    def _transform_input(self, compound, spacegroup, T):
        """
        Transform user input into the correct form for the model.

        Transforms `compound` and `spacegroup` into separate
        numpy.arrays of features, joins them, and scales it using
        the same scaler that was used on the training set.

        Args:
            compound (str): Chemical formula of material of interest.
            spacegroup (int or float): Space group number of material of
                interest.
            T (int or float): Temperature of interest.

        Returns:
            float: Scaled numpy.array of all compiled features.
        """
        cmpd_features = self._transform_compound(compound)
        sg_features = self._transform_spacegroup(spacegroup)
        joined_features = self._join_features(cmpd_features, sg_features, T)
        scaled_features = self._scale_features(joined_features)
        return scaled_features

    def _load_model(self):
        """
        Loads all objects required for model prediction.

        Loads the same scaler originally used on the training data.
        Loads in the two encoders for categorical data in the
        expanded spacegroup features. Lastly loads in the trained
        neural network.
        """
        self._load_scaler('scaler.save')
        self._load_encoder('encoder0.save', 0)
        self._load_encoder('encoder1.save', 1)
        self._load_neural_network('model.json', 'model.h5')
        return

    def _load_neural_network(self, json_file, weights_file):
        """
        Loads and compiles the trained neural network from
        the serialized json file and a weights file.

        Input:
        json_file, (string)
        weights_file, (string)

        Output:
        loaded_model, (keras.model)
        """
        assert isinstance (json_file, str), "json_file not entered as a string."
        assert isinstance (weights_file, str), "weights file not entered as a string."

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

        Args:
            scaler_file (str): Name of scaler file.
        """
        assert isinstance (scaler_file, str), "scaler_file not entered as string."
        self.scaler = joblib.load(file_path(scaler_file))
        return

    def _load_encoder(self, encoder_file, encoder_id):
        """
        Generates the two encoders used in space group information.

        Loads the encoder used for spacegroup information and creates
        two dictionaries. Each subdictionary contains an array of
        binary channels associated with the categorical data.

        Args:
            encoder_file (str): Name of the encoder file.
            encoder_id (int): ID used to identify which encoder is
                being addressed.
        """
        assert isinstance (encoder_file, str), "encoder_file not entered as string."
        assert isinstance (encoder_id, int), "encoder_id not entered as integer."
        loaded_encoder = joblib.load(file_path(encoder_file))
        encoder_dict = {}
        encoder_classes = np.array(loaded_encoder.classes_)
        for cl in encoder_classes:
            encoder_dict[cl] = [float(x) for x in cl == encoder_classes]
        self.encoder[encoder_id] = encoder_dict
        return

    def _replace_with_list_values(self, i, original, to_be_inserted):
        """
        Inserts values of a list into another list at index `i`

        Takes a list and inserts the values of the list into
        another list at a specified index `i` after deleting what
        was originally at index `i`.

        Args:
            i (int): Index location in list for replacement
            original (list): List containing value
                that will be replaced with values from another list.
            to_be_inserted (list of float): Elements in list will replace
                element in `original` at index `i`.

        Returns:
            list: `original` list after `to_be_inserted` values replaced
                item at index `i`.

        Raises:
            AssertionError: If `original` is not a list.
            AssertionError: If `to_be_inserted` is not a list.
        """
        assert isinstance (original, list), "original is not a list!"
        assert isinstance (to_be_inserted, list), "to_be_interserted is not a list!"

        del original[i]
        to_be_inserted.reverse()
        for value in to_be_inserted:
            original.insert(i, value)
        to_be_inserted.reverse()
        return original

    def _transform_spacegroup(self, spacegroup):
        """
        Transfroms the space group number to additional features.

        Creates a numpy.ndarray of space group features with any
        categorical data being expanded to multiple binary channels.

        Args:
            spacegroup (int): Space group number

        Returns:
            numpy.ndarray: Numerical array of space group features

        Raises:
            AssertionError: If `spacegroup` is not an int.
        """
        assert isinstance (spacegroup, int), "Input is not an integer!"

        sg_features = list(expand_spacegroup(spacegroup))
        for i in np.arange(2, 0, -1):
            extra_channels = self.encoder[i-1][sg_features[i]]
            sg_features = self._replace_with_list_values(i, sg_features,
                                                         extra_channels)
        return np.array(sg_features)

    def _transform_compound(self, compound):
        """
        Transforms chemical formula to an array up to 80 features.

        Converts one sample to raw data for predicting thru ANN.

        Args:
            compound (str): Chemical formula.

        Returns:
            numpy.ndarray: Descriptors for all elements in the chemical
                formula.

        Raises:
            AssertionError: If `compound` is not a str.
        """
        assert isinstance (compound, str), "Input is not a string!"
        cmpd_features = np.array(compound_short_descriptors(compound),
                                 dtype=np.float)
        cmpd_features = np.pad(cmpd_features, (0, 80-cmpd_features.shape[0]),
                               mode='constant')
        cmpd_features = np.nan_to_num(cmpd_features)

        return cmpd_features

    def _join_features(self, cmpd_features, sg_features, T):
        """
        Joins together the features of the compound, space group, and T.

        Args:
            cmpd_features (numpy.ndarray): Features describing the
                compound.
            sg_features (numpy.ndarray): Features describing the
                space group.
            T (int or float): Temperature of interest.

        Returns:
            numpy.ndarray: A single numpy array with all three feature
                vectors concatenated together.
        """
        return np.concatenate((cmpd_features, [T], sg_features))

    def _scale_features(self, features):
        """
        Scales the input feature vector with the proper scaler.

        Args:
            features (numpy.ndarray): All descriptors for the user's
                input.

        Returns:
            numpy.ndarray: Reshaped and scaled feature vector that
                is ready to be fed into the trained neural netowrk.

        Raises:
            AssertionError: If `features` is not a numpy.ndarray.
        """
        assert isinstance (features, np.ndarray), "Input is not a numpy array!"

        return self.scaler.transform(features.reshape(1, -1))


nn = TEMANN()


def predict_seebeck(compound, spacegroup, T):
    """
    Uses a trained neural network to predict Seebeck coefficient.

    Instantiates a TEMANN object and passes the arguments into
    TEMANN.predict() method to predict a Seebeck coefficient for the
    material of interest.

    Args:
        compound (str): Chemical formula of material of interest.
        spacegroup (int or float): Space group number of material of
            interest.
        T (int or float): Temperature of interest.

    Returns:
        float: Predicted Seebeck coefficient.

    Raises:
        TypeError: If `compound` is not a string.
        TypeError: If `spacegroup` is not an int or float.
        TypeError: If `T` is not an int or float.
        Exception: If `compound` contains more than 5
            unique elements.
    """

    if not isinstance(compound, str):
        raise TypeError("'compound` must be a string")
    else:
        pass

    if not isinstance(spacegroup, (int, float)):
        raise TypeError("'spacegroup' must be an int or float")
    else:
        pass

    if not isinstance(T, (int, float)):
        raise TypeError("'T' must be an int or float")
    else:
        pass

    if len(list(get_empirical_formula(compound).keys())) > 5:
        raise Exception('Too many unique elements',
                        'Compound must contain 5 or fewer elements!')

    return nn.predict(compound, spacegroup, T)

