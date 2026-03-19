-- init.sql
CREATE TABLE IF NOT EXISTS AppData (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert dummy data (Optional)
INSERT INTO AppData (content) VALUES ('Initial Database Row');
