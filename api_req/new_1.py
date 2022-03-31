import requests

#responce = requests.get("https://playground.learnqa.ru/api/hello")
#responce = requests.get("https://playground.learnqa.ru/api/get_500")
#responce = requests.get("https://playground.learnqa.ru/api/something")
responce = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)

print(responce.status_code)
print()
print(responce.text)
