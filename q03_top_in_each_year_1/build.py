# %load q03_top_in_each_year_1/build.py
import numpy as np
import pandas as pd
from collections import Counter

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q03_top_in_each_year_1(data):
    c = np.unique(data['Name'])
    a_dict = dict(zip(c, data.Count))
    return a_dict
