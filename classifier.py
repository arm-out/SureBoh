import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

df = pd.read_pickle('Data/df1.pickle')
print(df.head())
