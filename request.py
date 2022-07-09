import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Maintenance_cost':6000, 'Marketing_cost':5000, 'Salary_of_the_trainer':3500,'Duration_of_coaching_in_Hours':120,'Salary_of_the_trainer':15000,'Mode_of_Class':7,'Location':3,'Level_of_Course':0})

print(r.json())