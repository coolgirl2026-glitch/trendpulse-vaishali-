#step 1- import libararies

import pandas as pd

#step 2- load json file

file_path = "data/trends_20260403.json"
df = pd.read_json(file_path)

print("Data loaded successfully")


#step 3- check data

print(df.head())
print(df.info())
print(df.isnull().sum())

#step 4- clean data

print(df.duplicated())
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

#step 5- save cleaned data

output_file = "data/cleaned_trends.csv"

df.to_csv(output_file, index = False)

print(f"cleaned data saved to {output_file}")
