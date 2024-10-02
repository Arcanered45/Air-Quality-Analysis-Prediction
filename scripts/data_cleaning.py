import pandas as pd


raw_data = pd.read_csv('../data/raw_data.csv')


cleaned_data = raw_data.dropna()


# cleaned_data = cleaned_data[cleaned_data['PM2.5'] < threshold_value]


cleaned_data.to_csv('../data/cleaned_data.csv', index=False)
print("Data cleaned and saved as cleaned_data.csv!")
