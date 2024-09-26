import streamlit as st
import requests

# Function to get weather data
def get_weather():
    url = "https://api-open.data.gov.sg/v2/real-time/api/four-day-outlook"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit app layout
st.title("Singapore Weather Forecast App")

if st.button("Get Weather Outlook"):
    weather_data = get_weather()
    if weather_data:
        st.write("### 4-Day Weather Outlook")
        
        records = weather_data['data']['records']
        for record in records:
            date = record['date']
            for forecast in record['forecasts']:
                st.write(f"**Date:** {date} ({forecast['day']})")
                st.write(f"**Forecast:** {forecast['forecast']['text']}")
                st.write(f"**Summary:** {forecast['forecast']['summary']}")
                st.write(f"**Temperature (°C):** {forecast['temperature']['low']} - {forecast['temperature']['high']}")
                st.write(f"**Humidity:** {forecast['relativeHumidity']['low']}% - {forecast['relativeHumidity']['high']}%")
                st.write(f"**Wind Speed (km/h):** {forecast['wind']['speed']['low']} - {forecast['wind']['speed']['high']}")
                st.write("---")
    else:
        st.error("Could not retrieve weather data. Please try again later.")
