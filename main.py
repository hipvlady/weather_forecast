import streamlit as st
import plotly.express as px
from services import get_weather_data

st.title("Weather forecast for the next days")

place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of days to forecast")
data_type = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{data_type} for the next {days} days in {place}")

if place:
    weather_data = get_weather_data(place, days)

    if weather_data is None:
        st.error("City not found, please check the spelling")
    else:
        dates = [data["dt_txt"] for data in weather_data]

        if data_type == "Temperature":
            temperatures = [data["main"]["temp"] / 10 for data in weather_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (Celsius)"})
            st.plotly_chart(figure)

        elif data_type == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [data["weather"][0]["main"] for data in weather_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
