import requests
import json

url = "https://api-football-v1.p.rapidapi.com/v3/standings"

querystring = {"season":"2021", "league":"78"}

headers = {
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "68cd65fa40mshd0152fc63f9e5fep151d51jsn9ca3f6ffeb04"}

response = requests.request("GET", url, headers=headers, params=querystring)


result_json = response.text
res = json.loads(result_json)
res = response.json()['response'][0]['league']['standings'][0]
res_structured = json.dumps(res, indent=4)


for i in range(len(res)):
    team_info = res[i]
    team_name = team_info['team']['name']
    team_id = team_info['team']['id']
    team_rank = team_info['rank']
    team_logo = team_info['team']['logo']
    team_points = team_info['points']
    team_wins = team_info['all']['win']
    team_draw = team_info['all']['draw']
    team_lose = team_info['all']['lose']
    team_goals = team_info['all']['goals']['for']
    team_goals_conceded = team_info['all']['goals']['against']
    print(team_id, team_rank, team_name, team_logo, team_points, team_wins, team_draw, team_lose, team_goals, team_goals_conceded)
    # print(team_info)