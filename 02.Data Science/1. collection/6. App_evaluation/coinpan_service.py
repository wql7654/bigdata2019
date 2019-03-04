import requests

url = "https://gall.dcinside.com/board/lists/?id=bitcoins"

response = requests.request("GET", url)

print(response.text)