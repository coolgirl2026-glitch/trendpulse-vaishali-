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

# step 4 - remove duplicates
df = df.drop_duplicates()
print(f"After removing duplicates: {len(df)}")

# step 5 - remove null values
df = df.dropna()
print(f"After removing nulls: {len(df)}")

# step 6- remove low score posts
df = df[df["score"] > 50]
print(f"After removing low scores: {len(df)}")

# step 7 - save cleaned data
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} rows to {output_file}")

# step 8 - stories per category
print("\nStories per category:")
print(df["category"].value_counts())