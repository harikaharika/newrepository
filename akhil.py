import requests

req = requests.get('https://reqres.in/api/users?page=2')
print(req.json())

re1 = requests.get('https://reqres.in/api/users/2')
print(re1.json())

re2 = requests.get('https://reqres.in/api/users/23')
print(re2.json())

re3 = requests.get('https://reqres.in/api/unknown')
print(re3.json())

re4 = requests.get('https://reqres.in/api/unknown/2')
print(re4.json())

re5 = requests.get('https://reqres.in/api/unknown/23')
print(re5.json())

re6 = requests.get('https://reqres.in/api/users')
print(re6.json())

re7 = requests.get('https://reqres.in/api/users/2')
print(re7.json())

re8 = requests.get('https://reqres.in/api/users/2')
print(re8.json())

re9 = requests.get('https://reqres.in/api/register')
print(re9.json())

re10 = requests.get('https://reqres.in/api/register')
print(re10.json())

re11 = requests.get('https://reqres.in/api/login')
print(re11.json())

re12 = requests.get('https://reqres.in/api/login')
print(re12.json())

re13 = requests.get('https://reqres.in/api/users?delay=3')
print(re13.json())

