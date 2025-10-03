import requests
import time
from typing import Dict, Optional


class OpenWeatherRequest:
    def __init__(self, api_key: str, base_url: str = "http://api.openweathermap.org"):
        self.api_key = api_key
        self.base_url = base_url
        # Create a new session for each instance to avoid caching
        self.session = requests.Session()
        # Disable caching
        self.session.headers.update({
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        })

    def make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a GET request to OpenWeather API

        Args:
            endpoint (str): API endpoint
            params (Dict, optional): Additional query parameters

        Returns:
            Dict: JSON response from the API
        """
        if params is None:
            params = {}

        params['appid'] = self.api_key
        # Add timestamp to prevent caching
        params['_'] = int(time.time() * 1000)

        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.get(
                url,
                params=params,
                timeout=10,
                # Disable caching at request level
                headers={
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache'
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {str(e)}")
            return None

    def get_weather(self, lat: float, lon: float) -> Dict:
        """Get current weather data"""
        endpoint = "/data/2.5/weather"
        params = {
            'lat': lat,
            'lon': lon,
            'units': 'metric'
        }
        return self.make_request(endpoint, params)

    def get_air_pollution(self, lat: float, lon: float) -> Dict:
        """Get current air pollution data"""
        endpoint = "/data/2.5/air_pollution"
        params = {
            'lat': lat,
            'lon': lon
        }
        return self.make_request(endpoint, params)

    def get_air_pollution_history(self, lat: float, lon: float, start: int, end: int) -> Dict:
        """Get historical air pollution data"""
        endpoint = "/data/2.5/air_pollution/history"
        params = {
            'lat': lat,
            'lon': lon,
            'start': start,
            'end': end
        }
        return self.make_request(endpoint, params)