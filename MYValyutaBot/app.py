import requests
import json

inputs = str(input("ma'lumotlarni kiriting: "))
url = "https://v6.exchangerate-api.com/v6/5f6d43916b52307ea4aed1f3/latest/" + inputs

responses=requests.get(url)
rest = json.loads(responses.text)
print(rest["conversion_rates"]["UZS"])