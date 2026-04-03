#step 1- import libararies

import pandas as pd
import numpy as np

#step 2- loading cleaned data

file_path = "data/cleaned_trends.csv"

df = pd.read_csv(file_path)

print("data loaded successfully")
print(df.head())

#step 3- analysis

print("Total Post:", len(df))
print ("Average Score:", np.mean(df['score']))

top_commented = df.loc[df['num_comments'].idxmax()]

print("\nMost Commented Post:")
print(top_commented["title"])
print("comments:", top_commented["num_comments"])

print("\nTop categories:")
print(df["category"].value_counts())

top_score = df.loc[df["score"].idxmax()]

print("\nHighest scored post:")
print(top_score["title"])
print("Score:", top_score['score'])

print("\nAverage score per category:")
print(df.groupby("category")["score"].mean())



