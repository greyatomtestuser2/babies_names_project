# %load q01_create_dict/build.py
import pandas as pd
from collections import Counter

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q01_create_dict(data):
    a = dict(zip(data.Name, data.Count))
    return a
