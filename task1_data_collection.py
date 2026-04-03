#step 1- importing libraries

import requests
import json
import time
import os
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

#step 2- getting top story IDs from hackernews API

try:
    response = requests.get(TOP_STORIES_URL, headers=headers, timeout=10, verify=False)
    if response.status_code != 200:
        print("failed to fetch top stories")
    else:
        story_ids = response.json()[:1000]
    print("fetched top story IDs successfully")
except:
    print("error fetching top stories")
    story_ids =[]

#step 3- defining categories 

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film","music", "netflix", "game", "book", "show", "award", "streaming"],
    "others": []
}

#step 4- assigning category based on title

def assign_category(title):
    title = title.lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
                return category
        
    return None

#step 5- creating a storage for collected data

#list to store all stories
data = []  

#to count how many stories per category
category_counts = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0,
    "others": 0
}

#step 6- creating a loop to get through each story details and processing it

for story_id in story_ids:
    try:
        url = ITEM_URL.format(story_id)
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        if response.status_code != 200:
            print(f"failed request for {story_id}")
            continue
        story = response.json()

        #skip if not data
        if not story or "title" not in story:
            continue

        title = story.get("title", "")
        category = assign_category(title)

        if category is None:
            category = "others"

        #skip if category already has 25 stories
        if category_counts[category] >=25:
            continue
        
        print("processing:", title)
        
        #create a structured record
        record = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments":story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        #add to list
        data.append(record)

        #increase category count
        category_counts[category]+=1

        #if category reaches 25- wait for 2 sec
        if category_counts[category]==25:
            time.sleep(2)

        #stop when total reaches 125
        if len(data)>= 125:
            break

    except Exception as e:
        print(f"error fetching story {story_id}: {e}")

#step 7- save data to json file

#creating a data folder
if not os.path.exists("data"):
    os.makedirs("data")

#creating file name with-today's data
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

#save data to json file
with open(filename, "w") as f:
    json.dump(data, f, indent=4)

#print result
print(f"collected {len(data)} stories. saved to {filename}")

    


