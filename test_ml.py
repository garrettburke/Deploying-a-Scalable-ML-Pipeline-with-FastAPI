import pytest
from ml.model import load_model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def test_check_model_algorithm():
    """
    Check to ensure the model is using the RandomForestClassifier
    algorithm
    """
    model = load_model("./model/model.pkl")
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_all_data_used():
    """
    # add description for the second test
    """
    data = pd.read_csv("./data/census.csv")
    training_data, test_data = train_test_split(data, test_size=.2, random_state=42)
    training_data_shape = training_data.shape[0]
    test_data_shape = test_data.shape[0]
    assert (data.shape[0] - training_data_shape - test_data_shape) == 0


# TODO: implement the third test. Change the function name and input as needed
def test_check_test_split_data_types():
    """
    # add description for the third test
    """
    data = pd.read_csv("./data/census.csv")
    training_data, test_data = train_test_split(data, test_size=.2, random_state=42)
    assert isinstance(training_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
