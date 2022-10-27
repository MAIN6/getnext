import numpy as np
import pandas as pd


def load_graph_adj_mtx(path):
    """A.shape: (num_node, num_node), edge from row_index to col_index with weight"""
    A = np.loadtxt(path, delimiter=',')
    return A


def load_graph_node_features(path, feature1='checkin_cnt', feature2='poi_catid_code'):
    """X.shape: (num_node, 4), four features: checkin cnt, poi cat, latitude, longitude"""
    df = pd.read_csv(path, encoding='iso-8859-1')
    rlt_df = df[[feature1, feature2]]
    X = rlt_df.to_numpy()

    return X
