
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'playerid':1, 'strikeratemean':1, 'manofthematch':0,'5cketsinhand':6 ,'matchtype':3, 'inningstype':0, 'opposition':3, 'runs':54})

print(r.json())

