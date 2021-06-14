import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
for i in data:
    if i['userId']==7:
        print(i['title'])
