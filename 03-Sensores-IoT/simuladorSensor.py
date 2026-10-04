import requests
import random
import time

# La dirección de nuestra API en Flask
url = 'http://127.0.0.1:5000/sensores'

while True:
    # Creamos valores de temperatura y humedad
    temperatura = round(random.uniform(20, 30), 2)
    humedad = round(random.uniform(40, 60), 2)
    
    # Armamos el paquete de datos que vamos a enviar al servidor
    payload = {
        'temperatura': temperatura,
        'humedad': humedad,
        'timestamp': time.time()
    }
    
    # Enviamos el paquete al servidor
    response = requests.post(url, json=payload)
    
    # Mostramos en pantalla qué se mandó y si el servidor lo aceptó
    print(response, payload)
    
    # Esperamos 5 segundos para la siguiente lectura
    time.sleep(5)