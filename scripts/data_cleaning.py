import pandas as pd


raw_data = pd.read_csv('raw_data.csv')


cleaned_data = raw_data.dropna()





cleaned_data.to_csv('cleaned_data.csv', index=False)
print("Data cleaned and saved as cleaned_data.csv!")
