import requests

url = 'https://randomuser.me/api/'

def get_users_gender(n: int, gender: str):
    payload = {
        'gender': gender 
    }
    users = []
    for i in range(n):
        respons = requests.get(url=url, params=payload)
        if respons.status_code==200:
            data = respons.json()['results'][0]
            user = {
                'fullname': data['name']['first'] + ' ' + data['name']['last'],
                'gender': data['gender'],
                # 'email': data['email'],
                # 'phone': data['phone'],
                # 'image': data['picture']['medium'],
                # 'adress': data['location']['city'],
                # 'username': data['login']['username']
            }
            users.append(user)
        else:
            print('Status error')
    return users
print(get_users_gender(10, 'male'))