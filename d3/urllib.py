import urllib.request

# 1. Wprowadzenie do pracy z protokołem HTTP
# Pobieranie zawartości strony internetowej i wyświetlanie jej kodu źródłowego
url = "https://www.python.org"
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")
print(html)

# 2. Używanie urllib do wysyłania zapytań HTTP/HTTPS
# Pobieranie nagłówków odpowiedzi HTTP
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    headers = response.info()
    print(headers)

# 3. Biblioteka requests
# Pobieranie zawartości strony za pomocą biblioteki requests
import requests

response = requests.get("https://api.github.com/repos/python/cpython")
if response.status_code == 200:
    print(response.json())

# 4. Odczyt danych z internetu
# Pobieranie obrazu z internetu i zapisywanie go na dysku
image_url = "https://www.python.org/static/community_logos/python-logo.png"
image_response = requests.get(image_url)
if image_response.status_code == 200:
    with open("downloaded_image.png", "wb") as file:
        file.write(image_response.content)
    print("Obraz został pobrany i zapisany jako downloaded_image.png")
