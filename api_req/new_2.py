import json

string_as_json_format = '{"answer":"Hello, User"}'
obj = json.loads(string_as_json_format)

key = "answer2"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")

# import json
#
# string_as_json_format = '{"answer":"Hello, User"}'
# obj = json.loads(string_as_json_format)
# print(obj['answer'])
# #print(obj['answer2']) #negative test