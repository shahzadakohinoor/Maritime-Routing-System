DROP DATABASE IF EXISTS maritime_routing;
CREATE DATABASE maritime_routing;
USE maritime_routing;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(50) DEFAULT 'admin',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vessel (
    vessel_id INT PRIMARY KEY AUTO_INCREMENT,
    vessel_name VARCHAR(100) NOT NULL,
    dwt INT,
    draft FLOAT,
    speed FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE voyage (
    voyage_id INT PRIMARY KEY AUTO_INCREMENT,
    source_port VARCHAR(100),
    destination_port VARCHAR(100),
    distance_nm FLOAT,
    speed FLOAT,
    voyage_days FLOAT,
    fuel_used FLOAT,
    fuel_cost FLOAT,
    total_cost FLOAT,
    weather_risk VARCHAR(50),
    diversion_suggestion VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE weather (
    weather_id INT PRIMARY KEY AUTO_INCREMENT,
    wind_speed FLOAT,
    wave_height FLOAT,
    wave_direction FLOAT,
    wave_period FLOAT,
    gale_risk VARCHAR(50),
    sea_state VARCHAR(50),
    risk_level VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password, role)
VALUES ('admin', 'admin123', 'admin');

INSERT INTO vessel (vessel_name, dwt, draft, speed)
VALUES ('Sample Vessel', 50000, 12, 12);

INSERT INTO weather
(wind_speed, wave_height, wave_direction, wave_period, gale_risk, sea_state, risk_level)
VALUES
(32, 4.2, 240, 8, '18% - 22%', 'BF 7', 'High');

INSERT INTO voyage
(source_port, destination_port, distance_nm, speed, voyage_days, fuel_used, fuel_cost, total_cost, weather_risk, diversion_suggestion)
VALUES
('Rotterdam', 'Singapore', 8412, 12, 29.21, 934.67, 432750.67, 597750.67, 'High', '8° Southward Deviation Recommended');