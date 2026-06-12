import json

with open('data.json', 'r') as file:
    data = json.load(file)

# content is standard python dictionary 
skills = []
jobs_skills = []

print(data)