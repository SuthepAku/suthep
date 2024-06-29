from flask import Flask
from threading import Thread
import os

TOKEN = 'MTI1NjU2OTEwNDIzMjYxMTg1MA.GKsRMA.EnHrL4R3M6iuO_eP19KG9vrKvlrBrpnRX4Yi2c'

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

def run():
    port = int(os.getenv("PORT", 4000))
    app.run(host='0.0.0.0', port=port)

def server_on():
    t = Thread(target=run)
    t.start()


server_on()
