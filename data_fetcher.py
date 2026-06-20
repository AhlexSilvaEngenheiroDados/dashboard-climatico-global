import requests
import pandas as pd

def get_weather_data(lat, lon, city_name):
    """
    Busca dados meteorológicos reais da API Open-Meteo para uma localização específica.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Verifica se houve erro na requisição
        data = response.json()
        
        # Extrair dados atuais
        current = data['current_weather']
        
        return {
            "Cidade": city_name,
            "Temperatura": current['temperature'],
            "Vento": current['windspeed'],
            "Latitude": lat,
            "Longitude": lon
        }
    except Exception as e:
        print(f"Erro ao buscar dados para {city_name}: {e}")
        return None

def get_all_cities_data():
    """
    Coleta dados para uma lista de cidades pré-definidas.
    """
    cities = [
        {"name": "São Paulo", "lat": -23.55, "lon": -46.63},
        {"name": "Nova York", "lat": 40.71, "lon": -74.00},
        {"name": "Londres", "lat": 51.50, "lon": -0.12},
        {"name": "Tóquio", "lat": 35.68, "lon": 139.69},
        {"name": "Paris", "lat": 48.85, "lon": 2.35}
    ]
    
    results = []
    for city in cities:
        data = get_weather_data(city['lat'], city['lon'], city['name'])
        if data:
            results.append(data)
            
    return pd.DataFrame(results)

if __name__ == "__main__":
    df = get_all_cities_data()
    print("Dados coletados com sucesso:")
    print(df)
