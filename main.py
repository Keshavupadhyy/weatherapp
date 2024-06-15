import json
import requests
city= input("Enter the name of the city")
url=
r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])