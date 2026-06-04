# ── Adzuna API ──────────────────────────────────────────────────────────────
ADZUNA_APP_ID  = "your_app_id_here"
ADZUNA_APP_KEY = "your_app_key_here"
ADZUNA_BASE_URL = "https://api.adzuna.com/v1/api/jobs"
ADZUNA_COUNTRY  = "us"          # options: us, gb, ca, au, etc.

# ── Job search settings ──────────────────────────────────────────────────────
ROLES = [
    "data analyst",
    "data scientist",
    "data engineer",
]

RESULTS_PER_PAGE = 50           # max allowed by Adzuna is 50
PAGES_PER_ROLE   = 4            # 4 pages x 50 results = 200 postings per role

# ── PostgreSQL ───────────────────────────────────────────────────────────────
DB_HOST     = "localhost"
DB_PORT     = 5432
DB_NAME     = "skillradar"
DB_USER     = "postgres"
DB_PASSWORD = "your_password_here"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ── Output ───────────────────────────────────────────────────────────────────
RAW_DATA_PATH = "data/raw_jobs.json"    # where raw API results are saved