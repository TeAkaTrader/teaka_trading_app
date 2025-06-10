# Generate PostgreSQL CREATE TABLE scripts for the Teaka Trading Dashboard backend
sql_scripts = {
    "users.sql": """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    "api_keys.sql": """
    CREATE TABLE IF NOT EXISTS api_keys (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        exchange VARCHAR(50),
        api_key TEXT NOT NULL,
        api_secret TEXT NOT NULL,
        passphrase TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    "trade_logs.sql": """
    CREATE TABLE IF NOT EXISTS trade_logs (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        symbol VARCHAR(20),
        side VARCHAR(10), -- buy or sell
        amount DECIMAL,
        price DECIMAL,
        strategy VARCHAR(50),
        status VARCHAR(20),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    "strategies.sql": """
    CREATE TABLE IF NOT EXISTS strategies (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        description TEXT,
        config JSONB,
        user_id INTEGER REFERENCES users(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    "positions.sql": """
    CREATE TABLE IF NOT EXISTS positions (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        symbol VARCHAR(20),
        amount DECIMAL,
        entry_price DECIMAL,
        current_price DECIMAL,
        pnl DECIMAL,
        status VARCHAR(20),
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    "settings.sql": """
    CREATE TABLE IF NOT EXISTS settings (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        key VARCHAR(50),
        value TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    "market_data.sql": """
    CREATE TABLE IF NOT EXISTS market_data (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(20),
        price DECIMAL,
        volume_24h DECIMAL,
        change_24h DECIMAL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
}

import os

output_path = "/mnt/data/sql_teaka_dashboard"
os.makedirs(output_path, exist_ok=True)

for filename, script in sql_scripts.items():
    with open(os.path.join(output_path, filename), "w") as f:
        f.write(script.strip())

import ace_tools as tools; tools.display_files_from_path(output_path)
