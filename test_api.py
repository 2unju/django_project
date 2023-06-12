import requests

HOST = "http://127.0.0.1:8000"
res = requests.post(HOST + '/api-token-auth/', {
    'username': 'admin',
    'password': 'admin'
})

res.raise_for_status()
token = res.json()['token']
print(token)

headers = {'Authorization': "JWT" + token,
           'Accept': "application/json"}

data = {
    'title': "제목 by code",
    'text': 'API 내용 by code',
    "created_data": "2023-06-13T00:00:00+00:00",
    "published_data": "2023-06-13T00:00:00+00:00"
}
file = {'image': open("Users/E_N__/Downloads/IMG_9074.jpg", "rb")}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())