import requests

url = 'https://randomuser.me/api/'
respons = requests.get(url=url)
# print(data.status_code)
# print(type(data))

if respons.status_code==200:
    data = respons.json()['results'][0]
    text = respons.text
    user = {
        'fullname': data['name']['first'] + ' ' + data['name']['last'],
        'email': data['email'],
        'phone': data['phone'],
        'image': data['picture']['medium'],
        'adress': data['location']['city'],
        'username': data['login']['username']
    }
    print(user)
else:
    print('Status error')
    