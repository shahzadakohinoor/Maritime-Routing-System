CREATE DATABASE IF NOT EXISTS maritime_routing;
USE maritime_routing;

CREATE TABLE vessel (
    vessel_id INT PRIMARY KEY AUTO_INCREMENT,
    vessel_name VARCHAR(100),
    dwt INT,
    draft FLOAT,
    speed FLOAT
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
    gale_risk VARCHAR(50),
    sea_state VARCHAR(50),
    risk_level VARCHAR(50)
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100),
    password VARCHAR(100)
);

INSERT INTO users VALUES
(NULL, 'admin', 'admin123');

INSERT INTO vessel VALUES
(NULL, 'Sample Vessel', 50000, 12, 12);

INSERT INTO weather VALUES
(NULL, 32, 4.2, '18% - 22%', 'BF 7', 'High');