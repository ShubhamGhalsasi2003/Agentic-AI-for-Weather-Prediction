import os
import requests

def lambda_handler(event, context):
    API_KEY = os.environ['OPENWEATHER_API_KEY']
    lat = event.get('lat', 33.44)
    lon = event.get('lon', -94.04)
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    return {
        "statusCode": 200,
        "body": data
    }
