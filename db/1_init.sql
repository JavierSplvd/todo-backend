CREATE TABLE items (
    id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW(),
    created_at TIMESTAMP DEFAULT NOW()
);