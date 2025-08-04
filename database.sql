-- Users Table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    age INTEGER,
    gender TEXT,
    state TEXT,
    street_address TEXT,
    postal_code TEXT,
    city TEXT,
    country TEXT,
    latitude REAL,
    longitude REAL,
    traffic_source TEXT,
    created_at TEXT
);

-- Orders Table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    status TEXT,
    gender TEXT,
    created_at TEXT,
    returned_at TEXT,
    shipped_at TEXT,
    delivered_at TEXT,
    num_of_item INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


-- Total number of users
SELECT COUNT(*) FROM users;

-- Total number of orders
SELECT COUNT(*) FROM orders;

-- Sample joined data
SELECT o.order_id, u.first_name, u.last_name, o.status, o.num_of_item
FROM orders o
JOIN users u ON o.user_id = u.id
LIMIT 10;
