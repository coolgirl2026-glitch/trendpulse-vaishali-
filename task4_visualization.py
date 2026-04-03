#step 1- import libraries

import pandas as pd
import matplotlib.pyplot as plt

#step 2- loading cleaned data

file_path = "data/cleaned_trends.csv"
df = pd.read_csv(file_path)

print("data loaded successfully")

#step 3- create charts
#bar chart for categories

category_counts = df["category"].value_counts()
category_counts.plot(kind="bar")
plt.title("Top Categories")
plt.xlabel("Category")
plt.ylabel("Number of Posts")

plt.show()

#histogram of score

plt.hist(df["score"], bins=10)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.show()

#pie chart

category_counts.plot(kind="pie", autopct='%1.1f%%')
plt.title("Category Distribution")
plt.ylabel("")

plt.show()
