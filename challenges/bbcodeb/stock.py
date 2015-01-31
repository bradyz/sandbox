import requests
import json

url = 'http://requestb.in/vf3l6rvf'
payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get(url)

# GET with params in URL
r = requests.get(url, params=payload)

# POST with form-encoded data
r = requests.post(url, data=payload)

# POST with JSON
r = requests.post(url, data=json.dumps(payload))

# Response, status etc
print(r.text)
print(r.status_code)
