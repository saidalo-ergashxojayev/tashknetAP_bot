CREATE TABLE users (
    telegram_id BIGINT PRIMARY KEY,
    fullname VARCHAR(255),
    username VARCHAR(255),
    referrer_id BIGINT,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);