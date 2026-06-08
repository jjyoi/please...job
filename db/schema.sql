CREATE TABLE IF NOT EXISTS jobs (
    id          SERIAL PRIMARY KEY,
    role        VARCHAR(100),
    title       VARCHAR(255),
    company     VARCHAR(255),
    location    VARCHAR(255),
    description TEXT,
    created     VARCHAR(50),
    fetched_at  TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS skills (
    id          SERIAL PRIMARY KEY,
    skill_name  VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS job_skills (
    job_id      INT REFERENCES jobs(id),
    skill_id    INT REFERENCES skills(id),
    PRIMARY KEY (job_id, skill_id)
);