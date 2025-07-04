from flask import Flask
from prometheus_client import start_http_server, Summary, Counter
import time
import random

app = Flask(__name__)

# Métricas personalizadas
REQUEST_TIME = Summary('request_processing_seconds', 'Tiempo en procesar cada solicitud')
REQUEST_COUNTER = Counter('http_requests_total', 'Número total de solicitudes HTTP')

@app.route("/")
@REQUEST_TIME.time()
def hello():
    REQUEST_COUNTER.inc()
    delay = random.uniform(0.1, 0.9)
    time.sleep(delay)
    return f"¡Hola! Tiempo de respuesta: {delay:.2f} segundos"

if __name__ == "__main__":
    # Inicia el servidor de métricas (Prometheus recogerá de aquí)
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
