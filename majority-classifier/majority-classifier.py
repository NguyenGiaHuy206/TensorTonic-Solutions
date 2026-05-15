import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y_train = np.array(y_train)
    unique_value, counts = np.unique(y_train, return_counts = True)
    max_value = np.argmax(counts)
    result = np.full(len(X_test), unique_value[max_value])
    return result
    pass