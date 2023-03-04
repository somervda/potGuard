import uasyncio
import micropython
import sys
from microdot_asyncio import Microdot

import network
import time

ssid = 'guest24'
password = 'backyard'

wlan = network.WLAN(network.STA_IF)
app = Microdot()


@app.route('/')
async def hello(request):
    return 'Hello world'


def print_hello():
    print("Hello")


def start_server():

    try:
        # Connect to WLAN
        wlan.active(True)
        wlan.connect(ssid, password)
        print("Connecting:")
        while not wlan.isconnected() and wlan.status() >= 0:
            print(".", end="")
            time.sleep(1)

        print("Connected! IP Address = " + wlan.ifconfig()[0])
        # setup webserver
        print('Starting microdot app')
        print(micropython.mem_info())
        app.run(port=80)
    except:
        app.shutdown()
        wlan.disconnect()
        print("server shutdown. Exiting...")
        sys.exit(0)
