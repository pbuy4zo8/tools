'''
    written by K.Kobayashi(jeffy890)
    2024.06.28

    ip address sender

'''

import requests

url = "enter your desired address"
param = {
    "server_name": "enter your desired name to inform"
}

res = requests.get(url, params=param)
