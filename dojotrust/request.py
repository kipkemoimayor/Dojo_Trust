import requests

def location():
    response=requests.get("http://api.ipstack.com/105.27.206.46?access_key=18220f1e8b17fbf02d95d972679ccfef")
    geodata=response.json()
    return geodata
