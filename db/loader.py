import json
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    host     = "localhost",
    dbname   = "plsjob",
    user     = "postgres",
    password = os.getenv("DB_PASSWORD")
)
cur = conn.cursor()

with open("data.json", "r") as f:
    postings = json.load(f)

inserted = 0

for job in postings:
    cur.execute("""
        INSERT INTO jobs (role, title, company, location, description, created)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        job["role"],
        job["title"],
        job["company"],
        job["location"],
        job["description"],
        job["created"],
    ))
    inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"Inserted {inserted} jobs into the database.")