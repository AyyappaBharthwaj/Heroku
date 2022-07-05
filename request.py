import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Maintenance_cost':6000, 'Marketing_cost':5000, 'Profit_Margin':3500, 'Debentures':2500, 'Duration_of_coaching_in_Hours':120})

print(r.json())