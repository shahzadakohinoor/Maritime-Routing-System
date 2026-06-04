\# AI-Powered Maritime Weather Routing \& Voyage Optimization System



\## Project Overview



The AI-Powered Maritime Weather Routing \& Voyage Optimization System is a web-based application designed to help shipping operators optimize voyage planning by analyzing weather conditions, fuel consumption, voyage costs, ETA predictions, laycan compliance, and route diversion opportunities.



The system provides route recommendations based on weather risks and operational costs, helping vessel operators make safer and more economical voyage decisions.



\---



\## Objectives



\* Analyze weather conditions along maritime routes.

\* Calculate voyage duration and ETA.

\* Estimate fuel consumption and bunker costs.

\* Monitor laycan compliance risks.

\* Suggest alternate routes during adverse weather conditions.

\* Generate voyage performance reports.

\* Improve operational efficiency and safety.



\---



\## Features



\### Route Planning



\* Source and destination port selection.

\* Distance calculation.

\* Voyage duration estimation.



\### Weather Analysis



\* Weather risk monitoring.

\* Monsoon and storm detection.

\* Gale probability assessment.



\### Fuel Management



\* Daily fuel consumption calculation.

\* Total bunker consumption estimation.

\* Fuel cost analysis.



\### Cost Optimization



\* Voyage cost calculation.

\* Port and canal charges.

\* Carbon emission cost estimation.



\### Laycan Monitoring



\* ETA prediction.

\* Laycan compliance checking.

\* Delay risk alerts.



\### Route Diversion Recommendation



\* Weather avoidance routing.

\* Alternative route comparison.

\* Cost-benefit analysis of diversions.



\---



\## Technology Stack



\### Frontend



\* HTML5

\* CSS3

\* JavaScript

\* Bootstrap



\### Backend



\* Python Flask



\### Database



\* MySQL



\### APIs (Future Integration)



\* OpenWeather API

\* ERA5 Weather Data

\* Marine Traffic APIs



\---



\## Project Structure



```text

Maritime-Routing-System/

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

├── templates/

│   ├── index.html

│   ├── route.html

│   ├── weather.html

│   ├── report.html

│

├── database/

│   └── maritime.sql

│

├── app.py

├── requirements.txt

└── README.md

```



\---



\## Installation



\### Clone Repository



```bash

git clone <repository-url>

cd Maritime-Routing-System

```



\### Create Virtual Environment



```bash

python -m venv venv

```



\### Activate Virtual Environment



Windows:



```bash

venv\\Scripts\\activate

```



Linux/Mac:



```bash

source venv/bin/activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Run Application



```bash

python app.py

```



Open Browser:



```text

http://127.0.0.1:5000

```



\---



\## Database



Import the SQL file:



```sql

database/maritime.sql

```



into MySQL Workbench or phpMyAdmin.



\---



\## Future Enhancements



\* Real-time weather integration.

\* Interactive route visualization using Leaflet.

\* AI-powered route optimization.

\* Machine Learning-based fuel prediction.

\* Fleet management dashboard.

\* Carbon emission analytics.



\---



\## Author



\*\*Shahzada Kohinoor\*\*



BCA Student | Full Stack Developer | Data Analytics Enthusiast



\---



\## License



This project is developed for academic and internship purposes.



