from jsonrpcclient import request, parse, Ok
import requests


apiUrl = "https://alex.ia.utwente.nl/api/1/"

username = "idk"
password = "idk"

response = requests.post(apiUrl, json=request("login", params=(username, password)))

parsed = parse(response.json())
if isinstance(parsed, Ok):
    print(parsed.result)
else:
    logging.error(parsed.message)