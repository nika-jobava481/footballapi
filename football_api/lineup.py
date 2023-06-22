import requests
import json

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups"

querystring = {"fixture": "215662", "team": "463"}

headers = {
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "68cd65fa40mshd0152fc63f9e5fep151d51jsn9ca3f6ffeb04"}

response = requests.request("GET", url, headers=headers, params=querystring)


result_json = response.text
res = json.loads(result_json)
res = response.json()['response']
res_structured = json.dumps(res, indent=4)
# print(res_structured)


team_name = res[0]['team']['name']
team_logo = res[0]['team']['logo']
coach = res[0]['coach']['name']
coach_photo = res[0]['coach']['photo']
start_11 = res[0]['startXI']
print(team_name, team_logo,coach,coach_photo)


for i in range(len(start_11)):
    player_id = start_11[0]['player']['id']
    playar_name = start_11[0]['player']['name']
    playar_number = start_11[0]['player']['number']
    playar_position = start_11[0]['player']['pos']
    print(player_id, playar_name, playar_number, playar_position)