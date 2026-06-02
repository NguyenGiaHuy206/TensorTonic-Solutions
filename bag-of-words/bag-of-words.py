import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    word_count = {}

    for token in tokens:
        word_count[token] = word_count.get(token, 0) + 1

    return np.array([word_count.get(word, 0) for word in vocab], dtype=int)
    pass