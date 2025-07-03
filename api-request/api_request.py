import http
import requests

API_KEY = "a3cb0cb6f3c6b036aef74fa8d3641621"
API_COUNTRY = "Vietnam"
API_URL = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={API_COUNTRY}"

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        print("API response status code:", response.status_code)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


def mock_fetch_data():
    return {
        'request': {'type': 'City', 'query': 'Hanoi, Vietnam', 'language': 'en', 'unit': 'm'},
        'location': {
            'name': 'Hanoi',
            'country': 'Vietnam',
            'region': '',
            'lat': '21.033',
            'lon': '105.850',
            'timezone_id': 'Asia/Bangkok',
            'localtime': '2025-07-03 14:36',
            'localtime_epoch': 1751553360,
            'utc_offset': '7.0'
        },
        'current': {
            'observation_time': '07:36 AM',
            'temperature': 28,
            'weather_code': 296,
            'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0017_cloudy_with_light_rain.png'],
            'weather_descriptions': ['Light Rain'],
            'astro': {
                'sunrise': '05:20 AM',
                'sunset': '06:42 PM',
                'moonrise': '12:19 PM',
                'moonset': 'No moonset',
                'moon_phase': 'Waxing Gibbous',
                'moon_illumination': 52
            },
            'air_quality': {
                'co': '762.2',
                'no2': '45.14',
                'o3': '42',
                'so2': '25.16',
                'pm2_5': '37.925',
                'pm10': '39.775',
                'us-epa-index': '2',
                'gb-defra-index': '2'
            },
            'wind_speed': 7,
            'wind_degree': 121,
            'wind_dir': 'ESE',
            'pressure': 1006,
            'precip': 0.4,
            'humidity': 89,
            'cloudcover': 75,
            'feelslike': 31,
            'uv_index': 8,
            'visibility': 10,
            'is_day': 'yes'
        }
    }