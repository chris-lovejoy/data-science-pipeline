"""
A script to convert DataFrame into dataset with features, ready for training
"""

import numpy as np
import pandas as pd
from importlib.machinery import SourceFileLoader
import io


def build(subject_df):
    """

    """

    # Load config file
    config = SourceFileLoader("config","../config.py").load_module()

    # TODO: add code here which extracts features from subject_df and generates features_df

    return features_df

