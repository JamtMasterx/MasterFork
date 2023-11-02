import requests

ip = "45.230.216.249"
token = "fb90aad416b08b"
url = f"https://ipinfo.io/{ip}?token={token}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Recorre los elementos de data e imprime cada uno con un salto de línea
    for key, value in data.items():
        print(f"{key}: {value}\n")
else:
    print(f'Error en la solicitud: {response.status_code} - {response.text}')
