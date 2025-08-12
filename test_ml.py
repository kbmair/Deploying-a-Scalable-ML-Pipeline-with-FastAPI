import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import apply_label
from ml.model import train_model, compute_model_metrics
# TODO: add necessary import


# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    """
    # Your code here
    assert apply_label(np.array([1])) == ">50K"
    assert apply_label(np.array([0])) == "<=50K"


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    """
    # Your code here
    X_train = np.array([[0, 1], [1, 0]])
    y_train = np.array([0, 1])
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    # Precision = TP / (TP + FP) = 2 / 2 = 1.0
    assert np.isclose(precision, 1.0)
    # Recall = TP / (TP + FN) = 2 / 3 ≈ 0.6667
    assert np.isclose(recall, 2/3)
    # F1 score = 2 * (P * R) / (P + R) = 0.8
    assert np.isclose(fbeta, 0.8)
