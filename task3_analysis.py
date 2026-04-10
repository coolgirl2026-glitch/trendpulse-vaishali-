#step 1- import libararies

import pandas as pd
import numpy as np

#step 2- loading cleaned data

file_path = "data/cleaned_trends.csv"

df = pd.read_csv(file_path)

print("data loaded successfully")
print(df.head())
df["is popular"]= df["score"]>100

print("\nPopular posts:", df["is popular"].sum())

#step 3- analysis

print("\nAverage score:", int(np.mean(df["score"])))
print("Average comments:", int(np.mean(df["num_comments"])))

# NumPy stats
print("\n--- NumPy Stats ---")
print("Mean score:", int(np.mean(df["score"])))
print("Median score:", int(np.median(df["score"])))
print("Std deviation:", int(np.std(df["score"])))
print("Max score:", int(np.max(df["score"])))
print("Min score:", int(np.min(df["score"])))

# Category analysis
top_category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()
print(f"\nMost stories in: {top_category} ({count} stories)")

# Most commented
top_commented = df.loc[df["num_comments"].idxmax()]
print(f'\nMost commented story: "{top_commented["title"]}" — {top_commented["num_comments"]} comments')

# Save file
df.to_csv("data/trends_analysed.csv", index=False)
print("\nSaved to data/trends_analysed.csv")



