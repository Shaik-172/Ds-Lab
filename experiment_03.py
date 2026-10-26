# Experiment 3

import numpy as np
import pandas as pd

data = {'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan]}
df = pd.DataFrame(data)
print(df.isna())

df_clean = df.dropna()
df_filled = df.fillna(0)
print(df_clean)
print(df_filled)

df = pd.DataFrame({'gender': ['male', 'female', 'male']})
df['gender_num'] = df['gender'].map({'male': 0, 'female': 1})
df_renamed = df.rename(columns={'gender': 'Gender'})
print(df_renamed)

import numpy as np
data = pd.DataFrame(np.random.randn(100, 3))
outliers = (data > 3) | (data < -3)
print(outliers.sum())

import re

text = "This  is\t a\n test"
split_text = re.split(r'\s+', text)
print(split_text)

#Shaik Mohammed Khaja Nawaz
#23102A010352
#CSE(AI & ML)
