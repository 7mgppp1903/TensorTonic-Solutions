import numpy as np

def cosine_similarity(a, b):
    dot_product = np.dot(a,b)
    norm = np.linalg.norm(a) * np.linalg.norm(b)
    if norm == 0:
        return 0.0
    cosine = dot_product/norm
    
    return cosine
    pass