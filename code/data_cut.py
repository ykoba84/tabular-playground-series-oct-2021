import pandas as pd

data = pd.read_csv('../input/train.csv', nrows=100000)
data.to_csv('../output/train_set1.csv')
