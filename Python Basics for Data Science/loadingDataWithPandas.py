# Loading data with "pandas" library
import pandas as pd

csv_path = 'data.csv'
df = pd.read_csv(csv_path)
df.head()