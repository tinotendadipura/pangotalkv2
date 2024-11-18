import json
import requests

ENDPOINT = "http://127.0.0.1:8000/create/user"

headers = {"Content-Type":"application/json"}

data = {"username":"t30inotenda",
        "email":"tinotenda101000@gmail.com",
        "password":"tinotenda360"
         
}

r= requests.post(ENDPOINT , data = json.dumps(data),headers = headers)
print(r.text)