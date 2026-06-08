import os
import requests 
import json
import time
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")

# print(API_KEY)
# print(APP_ID)

ROLES = ["data analyst", "data scientist", "data engineer"]
PAGES = 4  

all_postings = []

for role in ROLES:
    print(f"Fetching: {role}")
    for page in range(1, PAGES + 1):
        url = f"https://api.adzuna.com/v1/api/jobs/us/search/{page}"
        params = {
            "app_id":           APP_ID,
            "app_key":          API_KEY,
            "results_per_page": 50,
            "what":             role,
        }
        response = requests.get(url, params=params).json()
        results  = response.get("results", [])

        for job in results:
            all_postings.append({
                "role":        role,
                "title":       job.get("title", ""),
                "company":     job.get("company", {}).get("display_name", ""),
                "location":    job.get("location", {}).get("display_name", ""),
                "description": job.get("description", ""),
                "created":     job.get("created", ""),
            })

        print(f"  Page {page}: {len(results)} results")
        time.sleep(0.5)

with open("data.json", "w") as f:
    json.dump(all_postings, f, indent=2)

print(f"\nDone. Total postings saved: {len(all_postings)}")
