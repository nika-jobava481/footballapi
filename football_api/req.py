import requests

url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2020","team":"33"}

headers = {
	"X-RapidAPI-Key": "018490ae74msh76daff5b99447f7p13d47ejsnc069ebcec164",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())