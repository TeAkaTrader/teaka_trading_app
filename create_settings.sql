CREATE TABLE IF NOT EXISTS settings (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    api_key TEXT,
    api_secret TEXT,
    strategy VARCHAR(50),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
