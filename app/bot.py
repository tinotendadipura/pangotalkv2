import requests

import json

url = "https://api.gupshup.io/sm/api/v1/msg"



payload = { "channel" : "whatsapp",
            "source" : "917834811114",
            "destination" : "dial_code",
            "src.name": "pangotalkClient",
            "message" : {
   "type":"text",
   "text":"Hello user, how are you?"
}
}
headers = {
    "Accept": "application/json",
    "apikey": "oloylotbm9qytlykdaugjdtjx6stdv2c",
    "Content-Type": "application/x-www-form-urlencoded"
}
# payload= json.dumps(payload, indent = 4) 
response = requests.post(url, data=payload, headers=headers)

print(response.text)