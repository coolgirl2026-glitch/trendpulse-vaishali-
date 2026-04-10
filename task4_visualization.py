#step 1- import libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

#step 2- loading cleaned data

file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

df["is_popular"]= df["score"]>100

print("data loaded successfully")

#step 3- create charts
# Chart 1: Top 10 Stories (Bar Chart)
top_stories = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top_stories["title"], top_stories["score"])
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Title")

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# Chart 2: Categories (Bar Chart)
category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar")

plt.title("Top Categories")
plt.xlabel("Category")
plt.ylabel("Number of Posts")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# Chart 3: Scatter Plot
plt.figure()

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# BONUS: Dashboard
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1
axs[0].barh(top_stories["title"], top_stories["score"])
axs[0].set_title("Top Stories")

# Chart 2
category_counts.plot(kind="bar", ax=axs[1])
axs[1].set_title("Categories")

# Chart 3
axs[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axs[2].set_title("Scatter Plot")
axs[2].legend()

plt.suptitle("TrendPulse Dashboard")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved successfully in outputs/ folder")