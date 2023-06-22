import json
import requests

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"team":"33", "season":"2020"}

headers = {
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "68cd65fa40mshd0152fc63f9e5fep151d51jsn9ca3f6ffeb04"}

response = requests.request("GET", url, headers=headers, params=querystring)


result_json = response.text
res = json.loads(result_json)
res = response.json()['response']
res_structured = json.dumps(res, indent=4)
# print(res_structured)

for i in range(len(res)):
    player_id = res[i]['player']['id']
    name = res[i]['player']['name']
    age = res[i]['player']['age']
    birthday = res[i]['player']['birth']['date']
    country = res[i]['player']['birth']['country']
    heigth = res[i]['player']['height']
    weight = res[i]['player']['weight']
    photo = res[i]['player']['photo']
    print(f"player id: {player_id}, name: {name}, age: {age}, birthday: {birthday}, "
          f"country: {country}, heigth: {heigth}, weight: {weight},"
          f"photo: {photo}")




