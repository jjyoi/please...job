# please...job!
- A data pipeline that tracks in demand skills across data roles
- powered by live job postings, NLP, and an interactive dashboard

## What It Does

please...job! pulls real job postings for **Data Analyst**, **Data Scientist**, and **Data Engineer** roles from a free jobs API, extracts and normalizes skill mentions (Python, SQL, Spark, AWS, etc.), stores everything in PostgreSQL, and surfaces the results in a Streamlit dashboard.

## How to Run 
1. Run `python db/loader.py`.
2. To verify it worked, run `psql -U postgres -d plsjob`
3. and inside psql run `SELECT role, COUNT(*) FROM jobs GROUP BY role;`. You should get a count of all data

**Key insights:**
...


## Requirements
Make sure PostgeSQL is installed on your device. 
