import requests

#responce = requests.get("https://playground.learnqa.ru/api/hello")
#responce = requests.get("https://playground.learnqa.ru/api/get_500")
#responce = requests.get("https://playground.learnqa.ru/api/something") #ОПЕЧАТКА В responCe, need S ! ! !
response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)

first_response = response.history[0]
second_response = response

print(first_response.url)
print(second_response.url)

#print(responce.status_code)
#print()
#print(responce.text)
