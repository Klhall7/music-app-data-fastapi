-- database music_app_data

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    allow_location_tracking BOOLEAN DEFAULT true, --optional privacy preference
    default_zip_code VARCHAR(20), -- Optional default ZIP code
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tokens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    token TEXT NOT NULL
);

CREATE TABLE location_data (
    id SERIAL PRIMARY KEY,  
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE, --associate location with a specific user
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    zip_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_zip_code ON location_data (zip_code); -- anticipate frequent lookups based on ZIP codes

CREATE TABLE IF NOT EXISTS playlist_data (
    playlist_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    playlist_name VARCHAR(100) NOT NULL,
    song VARCHAR(100) NOT NULL,
    album VARCHAR(100),
    artist VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS device_info (
    device_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    screen_size VARCHAR(50),
    network_connection VARCHAR(50),
    device_type VARCHAR(50),
    visitor_ip VARCHAR(50), -- take privacy settings into consideration
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS playlist_reviews (
    review_id SERIAL PRIMARY KEY,
    playlist_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (playlist_id) REFERENCES playlist_data(playlist_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);