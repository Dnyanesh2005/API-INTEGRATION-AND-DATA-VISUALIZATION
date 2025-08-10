
!pip install requests matplotlib seaborn

import requests
import pandas as pd
# Your actual API key
api_key = "26e9b1dfad5a450232f494977ce4cdc5"
# City for which you want weather data
city = "Mumbai"
# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
# Request weather data
response = requests.get(url)
if response.status_code == 200:
data = response.json()
# Extract relevant data
weather_data = {
"City": city,
"Temperature (°C)": data["main"]["temp"],
"Humidity (%)": data["main"]["humidity"],
"Pressure (hPa)": data["main"]["pressure"],
"Weather": data["weather"][0]["description"].capitalize()
}
# Convert to DataFrame
df = pd.DataFrame([weather_data])
print("\nCurrent Weather Data:\n")
print(df.to_string(index=False))
else:
print(f"Error {response.status_code}: {response.text}")


Current Weather Data:
 City Temperature (°C) Humidity (%) Pressure (hPa) Weather
Mumbai 30.99             66            1009        Haze


import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Your actual API key
api_key = "26e9b1dfad5a450232f494977ce4cdc5"
# City for which you want weather data
city = "Mumbai"
# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
# Request weather data
t t( l)
8/9/25, 2:28 PM Untitled8.ipynb - Colab
https://colab.research.google.com/drive/1nZKzjjK-GSbxJKvRXmos1p5dSPcSweUk#scrollTo=OByrtZ1SC81Y&printMode=true 2/3
nt Weather Data:
y Temperature (°C) Humidity (%) Pressure (hPa) Weather
i 30.99 70 1009 Haze
ipython-input-3423000079.py:38: FutureWarning:
ng `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. As
.barplot(
response = requests.get(url)
if response.status_code == 200:
data = response.json()
# Extract relevant data
weather_data = {
"City": city,
"Temperature (°C)": data["main"]["temp"],
"Humidity (%)": data["main"]["humidity"],
"Pressure (hPa)": data["main"]["pressure"],
"Weather": data["weather"][0]["description"].capitalize()
}
# Convert to DataFrame
df = pd.DataFrame([weather_data])
print("\nCurrent Weather Data:\n")
print(df.to_string(index=False))
# ===== Visualization =====
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(
x=["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"],
y=[df["Temperature (°C)"][0], df["Humidity (%)"][0], df["Pressure (hPa)"][0]],
palette="viridis"
)
plt.title(f"Weather Stats for {city}")
plt.ylabel("Values")
plt.show()
else:
print(f"Error {response.status_code}: {response.text}")



