import os
import requests


def get_api_key():
    api_key = os.environ.get('W_API_KEY')
    return api_key


def get_data(place, forecast_days=None, kind=None):
    api_key = get_api_key()
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        if kind == "Sky":
            filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(f"W_API_KEY is {get_api_key()}")
    print(get_data(place="Kyiv", forecast_days=3, kind="Temperature"))
