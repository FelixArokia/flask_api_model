import requests

url = 'http://localhost:5000/model_predict/'

data = [[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0]]
json_data = {"data": data}
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, json=json_data, headers=headers)
print(r,r.text)