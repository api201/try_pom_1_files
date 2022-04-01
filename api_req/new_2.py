import json

string_as_json_format = '{"answer":"Hello, User"}'
obj = json.loads(string_as_json_format)
print(obj['answer'])
#print(obj['answer2']) #negative test