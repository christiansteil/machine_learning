import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(columns=['column1'])

# NUMERICAL DATA

# Standardize data: mean=0, std=1
from sklearn.preprocessing import StandardScaler

# Normalize data: min=0, max=1
from sklearn.preprocessing import MinMaxScaler

# Logarithmic transformation: make right-skewed data (few data points on right side) closer to a normalized distribution,
# also reduces size of data values
np.log(data['column1'])

# CATEGORICAL DATA

# Nominal data: data that has no particular order or hierarchy to it

# One hot encoding: assign dummy values for each category
# ex. if categories are red, blue and green, red=[1,0,0] blue=[0,1,0] green=[0,0,1]
from sklearn.preprocessing import OneHotEncoder

# Ordinal data: categorical data where the categories have order, but the differences between the categories are not important or unclear
# think car conditions - categories can be sorted by newest to oldest

from sklearn.preprocessing import OrdinalEncoder
 
