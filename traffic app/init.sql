CREATE DATABASE IF NOT EXISTS traffic_db;

USE traffic_db;

CREATE TABLE IF NOT EXISTS traffic_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_count INT,
    time_of_day VARCHAR(20),
    prediction VARCHAR(20)
);
