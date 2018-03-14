import numpy as np

from ..prediction import *


def test_predict_seebeck():

    try:
        predict_seebeck(1234, 62, 400)
    except(TypeError):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when `compound` isn't a string")

    try:
        predict_seebeck('CaMnO3', 62.0, 400)
    except(TypeError):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when `spacegroup` isn't an int")

    try:
        predict_seebeck('CaMnO3', 62, '400')
    except(TypeError):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when `T` isn't an int or float")

    try:
        predict_seebeck('CaLaTiLiMnO3', 62, 400)
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when too many elements are passed")

    try:
        predict_seebeck('CaMnO3', 240, 400)
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when `spacegroup`" +
                        " is greater than 230")
    return


def test_scale_features_1():
    nn = TEMANN()
    try:
        nn._scale_features('12345')
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when input is not numpy array")
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
        nn._transform_compound(1234)
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when input is not a string")
    return


def test_transform_spacegroup_1():
    nn = TEMANN()
    output = nn._transform_spacegroup(221)
    assert len(output) == 14, "Not all spacegroup features transformed."
    return


def test_transform_spacegroup_2():
    nn = TEMANN()
    try:
        nn._transform_spacegroup(221.0)
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when input is not an integer")
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
    try:
        nn._replace_with_list_values(1, list1, 'A')
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when input is not a list")
    return


def test_load_encoder_1():
    nn = TEMANN()
    encoder_file = 1234
    encoder_id = '0'
    try:
        nn._load_encoder(encoder_file, encoder_id)
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when encoder_file input in not" +
                        " a string, or encoder_id is not an int")
    return


def test_load_scaler_1():
    nn = TEMANN()
    scaler_file = 1234
    try:
        nn._load_scaler(scaler_file)
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when scaler_file is not a string.")
    return


def test_load_neural_network_1():
    nn = TEMANN()
    json_file = 1234
    weights_file = 5678
    try:
        nn._load_neural_network(json_file, 'model.h5')
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when json_file is not a string.")

    try:
        nn._load_neural_network('model.json', weights_file)
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when weights_file is not a string.")
    return
