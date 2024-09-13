-- Create the users table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Insert 10 random users into the users table
INSERT INTO users (name, email) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com'),
('Alice Johnson', 'alice.johnson@example.com'),
('Bob Brown', 'bob.brown@example.com'),
('Charlie White', 'charlie.white@example.com'),
('Emily Davis', 'emily.davis@example.com'),
('Frank Wilson', 'frank.wilson@example.com'),
('Grace Lee', 'grace.lee@example.com'),
('Henry Clark', 'henry.clark@example.com'),
('Ivy Walker', 'ivy.walker@example.com');
