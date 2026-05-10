#  Flask Weather App


**Live Demo:** [Weatherapp](https://weather-app-jqtd.onrender.com)

A simple weather web application built using Flask that fetches real-time weather data using the OpenWeather API.

---

##  Features

- Search weather by city 
- Displays:
  - Temperature   
  - Feels like temperature   
  - Weather condition  
- Handles invalid city inputs gracefully 
- Clean and minimal UI 

---

##  Tech Stack

- Python   
- Flask  
- HTML + CSS   
- OpenWeather API   
- Waitress (Production server)

---

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/pallavihegde01/weather-app.git
cd weather-app
```
### 2. Create virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install flask requests python-dotenv waitress
```

### 4. Add your API key
Create a .env file in the root directory:
```bash
API_KEY=your_openweather_api_key
```

### 5. Run the app
```bash
python server.py
```
App will run on: http://localhost:8000
