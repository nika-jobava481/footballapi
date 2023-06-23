import requests

url = "https://api-football-v1.p.rapidapi.com/v3/players/squads"

def getSquad(id):
    querystring = {"team":id}

    headers = {
        "X-RapidAPI-Key": "018490ae74msh76daff5b99447f7p13d47ejsnc069ebcec164",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring).json()['response'][0]['players']

    return response
