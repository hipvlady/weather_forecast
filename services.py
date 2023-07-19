import os
import requests
import streamlit as st


def get_api_key():
    api_key = os.environ.get('W_API_KEY')
    if not api_key:
        st.error("Error: API key is not set.")
        return None
    return api_key


def get_weather_data(place, forecast_days=None):
    api_key = get_api_key()
    if api_key is None:
        return None

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        st.error(f"Error: The API request failed with status code {response.status_code}")
        return None

    data = response.json()
    try:
        filtered_data = data["list"][:8 * forecast_days] if forecast_days else data["list"]
    except KeyError:
        st.error("Error: 'list' key not found in the data.")
        return None

    return filtered_data


if __name__ == '__main__':
    print(f"W_API_KEY is {get_api_key()}")
    print(get_weather_data(place="Kyiv", forecast_days=3))
