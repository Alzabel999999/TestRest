import requests
import json

data = {
    'username': 'aries',
    'password': 'aries'
}
ss = requests.post('http://127.0.0.1:8000/auth/jwt/create/', data=data)
print(ss.json())
print(ss.json()['access'])
data1 = {
    'Authorization': 'Bearer' + ' ' + ss.json()['access']
}
ss1 = requests.get('http://127.0.0.1:8000/auth/users/me/', headers=data1)
print(ss1.json())
ss5 = requests.get('http://127.0.0.1:8000/auth/users/logout/', headers=data1)
print(ss5.json())
data3 = {
    'email': 'alzabel999999@gmail.com',
    'username': 'Alzabel',
    'password': 'Darkaries110490'
}
ss3 = requests.post('http://127.0.0.1:8000/auth/users/', data=data3)
print(ss3.json())
ss4 = requests.get('http://127.0.0.1:8000/api/accounts/all-profiles', headers=data1)
print(ss4.json())