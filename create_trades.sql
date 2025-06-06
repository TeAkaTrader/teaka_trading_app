CREATE TABLE IF NOT EXISTS trades (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    exchange VARCHAR(50),
    pair VARCHAR(20),
    trade_type VARCHAR(10),
    price NUMERIC(18,8),
    quantity NUMERIC(18,8),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
