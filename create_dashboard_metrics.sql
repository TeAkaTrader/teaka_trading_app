CREATE TABLE IF NOT EXISTS dashboard_metrics (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    pnl NUMERIC(18,2),
    win_rate NUMERIC(5,2),
    trades_count INT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
