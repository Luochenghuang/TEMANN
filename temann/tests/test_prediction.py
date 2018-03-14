import numpy as np

from ..prediction import *


def test_predict_seebeck():

    assert False
    return

def test_scale_features_1():
    nn = TEMANN()
    try:
        nn._scale_features(np.random.randint(10, size=95))
    except(Exception):
        raise Exception ("Bad input allowed",
                        "Error not raised when input is not numpy array")  
    else:
        pass
    return

def test_transform_compound_1():
    nn = TEMANN()
    compound = "CaMnO3"
    output = nn._transform_compound(compound)
    assert len(output) == 80,  "Padding of np array not completed"
    return

def test_transform_compound_2():
    nn = TEMANN()
    try:
        nn._transform_compound('CaMnO3')
    except(Exception):
        raise Exception ("Bad input allowed",
                        "Error not raised when input is not a string")
    else:
        pass
    return

def test_transform_spacegroup_1():
    nn = TEMANN()
    output = nn._transform_spacegroup(221)
    assert len(output) == 14, "Not all spacegroup features transformed."
    return

def test_transform_spacegroup_2():
    nn = TEMANN()
    try:
        nn._transform_spacegroup(221)
    except(Exception):
        raise Exception ("Bad input allowed",
                        "Error not raised when input is not an integer")
    else:
        pass
    return

def test_replace_with_list_values_1():
    nn = TEMANN()
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = ['A', 'B']
    nn._replace_with_list_values(1, list1, list2)
    assert len(list1) > len(list2), 'Original list not modified correctly, check that\
                                    to be inserted is not empty'
    return

def test_replace_with_list_values_2():
    nn = TEMANN()
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = ['A', 'B']
    try:
        nn._replace_with_list_values(1, list1, list2)
    except(Exception):
        raise Exception ("Bad input allowed",
                        "Error not raised when input is not a list")
    else:
        pass
    return
def test_load_encoder_1():
    nn = TEMANN()
    encoder_file = 'encoder0.save'
    encoder_id = 0
    try:
        nn._load_encoder(encoder_file, encoder_id)
    except(Exception):
        raise Exception ("Bad input allowed",
                        "Error not raised when encoder_file input in not\
                         a string, or encoder_id is not an int")
    else:
        pass
    return

def test_load_scaler_1():
    nn = TEMANN()
    scaler_file = 'scaler.save'
    try:
        nn._load_scaler(scaler_file)
    except(Exception):
        raise Exception ("Bad input allowed",
                        "Error not raised when scaler_file is not a string.")
    else:
        pass
    return

def test_load_neural_network_1():
    nn = TEMANN()
    json_file = 'model.json'
    weights_file = 'model.h5'
    try:
        nn._load_neural_network(json_file, weights_file)
    except(Exception):
        raise Exception ("Bad input allowed",
                        "Error not raised when scaler_file is not a string.")
    else:
        pass
    return

