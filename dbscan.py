'''
DBSCAN: Density-Based Spatial Clustering of Applications with Noise

Documentation for original:
https://github.com/scikit-learn/scikit-learn/blob/0fb307bf3/sklearn/cluster/_dbscan.py#L150
'''

import numpy as np

def dbscan():
    '''
    TODO:
        - Figure out callable parameters ^
        -
    '''
    # estimate = DBSCAN(parameters here)
    # estimate.fit
    pass

class DBSCAN():
    '''
    TODO:
        - Figure out callable parameters
        - Define fit() method
        - Define predict() method
    '''
    '''
    dist = maximum distance between neighbors (same cluster)
    min_points = minimum number of points required to be considered for a cluster
    '''
    def __init__(self, dist=.1, min_points=5):
        self.dist = dist
        self.min_samples = min_samples

    def fit():
        pass

    def predict():
        pass
