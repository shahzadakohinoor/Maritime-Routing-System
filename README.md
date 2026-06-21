# 🚢 AI-Powered Maritime Weather Routing & Voyage Optimization System
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Project Overview

The AI-Powered Maritime Weather Routing & Voyage Optimization System is a web-based application designed to assist shipping operators in planning safer and more economical voyages.

The system analyzes voyage routes, weather conditions, fuel consumption, voyage costs, ETA predictions, laycan compliance, and route diversion opportunities to improve operational efficiency and maritime safety.

---

## Key Features

### 🌍 Route Planning

* Source and destination port selection
* Distance calculation
* Voyage duration estimation
* ETA prediction

### 🌦 Weather Analysis

* Marine weather monitoring
* Wave height analysis
* Weather risk assessment
* Monsoon and storm impact evaluation

### ⛽ Fuel Management

* Fuel consumption estimation
* Bunker cost calculation
* Voyage fuel optimization

### 💰 Cost Optimization

* Fuel cost analysis
* Port charges calculation
* Canal transit cost estimation
* Total voyage cost computation

### 🚨 Route Diversion Recommendation

* Weather-based routing
* Risk reduction suggestions
* Cost-benefit analysis

### 📊 Voyage History

* Historical voyage records
* Route performance tracking
* Cost comparison

### 🚢 Vessel Management

* Vessel registration
* Fleet monitoring
* Vessel specifications management

### 🔐 Admin Dashboard

* Secure login system
* Voyage statistics
* Fleet statistics
* Operational monitoring

### 📄 PDF Report Generation

* Voyage summary reports
* Downloadable PDF reports
* Performance documentation

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* Python
* Flask

### Database

* MySQL

### APIs

* Open-Meteo Marine Weather API

### Deployment

* Render

---

## Project Structure

```text
Maritime-Routing-System/
│
├── app.py
├── db_config.py
├── requirements.txt
├── Procfile
├── README.md
│
├── database/
│   └── maritime.sql
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
└── templates/
    ├── index.html
    ├── route.html
    ├── weather.html
    ├── history.html
    ├── vessel.html
    ├── login.html
    ├── admin.html
    ├── map.html
    └── report.html
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/shahzadakohinoor/Maritime-Routing-System.git
cd Maritime-Routing-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Database Setup

### Create Database

```sql
CREATE DATABASE maritime_routing;
```

### Import SQL File

```text
database/maritime.sql
```

Import using phpMyAdmin or MySQL Workbench.

---

## Default Admin Login

```text
Username: admin
Password: admin123
```

---

## Future Enhancements

* AI-based route optimization engine
* Machine learning fuel prediction
* Real-time vessel tracking
* Carbon emission analytics
* Fleet management dashboard
* Advanced weather forecasting
* Interactive GIS mapping
* Voyage performance benchmarking

---

## Screenshots

Add screenshots of:

* Home Page
* Route Calculator
* Weather Dashboard
* Voyage Map
* Voyage History
* Admin Dashboard

---

## Author

**Shahzada Kohinoor**

BCA Student | Full Stack Developer | Data Analytics Enthusiast

GitHub: https://github.com/shahzadakohinoor

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
© 2026 Shahzada Kohinoor. All Rights Reserved.

---

## Acknowledgements

* Flask Framework
* Open-Meteo Marine API
* MySQL Database
* Render Hosting Platform
* OpenStreetMap & Leaflet Maps
