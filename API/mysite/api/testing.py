import json
import urllib.request

bird_array = []

with urllib.request.urlopen("http://127.0.0.1:8000/bird") as url:
    data = json.loads(url.read().decode())

for i in data:
    list1 = i.values()
    list_list = list(list1)
    bird_array.append(list_list[1])
print(bird_array)
