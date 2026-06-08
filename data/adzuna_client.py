import os
import requests 
import json
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")

print(API_KEY)
print(APP_ID)

response = requests.get(f'https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={APP_ID}&app_key={API_KEY}').json()


with open("data.json", "w") as file:
    json.dump(response, file)
