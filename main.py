import requests

url = 'https://randomuser.me/api/'
data = requests.get(url=url)
print(data.status_code)
print(type(data))

if data.status_code==200:
    data = data.json()
    print(data)
else:
    print('Status error')
    