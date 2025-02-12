import requests
import json

# 1. Jak działa API? (Prosty przykład pobrania danych z API)
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# 2. Wysyłanie zapytań za pomocą HTTP (GET, POST)
url_post = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}
response_post = requests.post(url_post, json=data)
print("POST Response:", response_post.json())

# 3. Praca z danymi JSON - parsowanie i tworzenie zapytań
json_data = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = json.loads(json_data)
print("Parsed JSON:", parsed_data)
new_json = json.dumps(parsed_data)
print("New JSON:", new_json)

# 4. Przykład użycia zewnętrznego API (pobieranie danych pogodowych z Open-Meteo)
latitude = 51.5074
longitude = -0.1278
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
weather_response = requests.get(weather_url)
if weather_response.status_code == 200:
    weather_data = weather_response.json()
    print("Weather in London:", weather_data["current_weather"])
else:
    print("Error fetching weather data")

# 5. Obsługa błędów i timeout w zapytaniach API
try:
    response_timeout = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=5)
    response_timeout.raise_for_status()  # Rzuca wyjątek przy błędzie HTTP
    print("Response with Timeout Handling:", response_timeout.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
