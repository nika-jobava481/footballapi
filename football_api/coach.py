import requests

url = "https://api-football-v1.p.rapidapi.com/v3/coachs"
def getCoachByTeam(id):
    querystring = {"team":id}

    headers = {
        "X-RapidAPI-Key": "018490ae74msh76daff5b99447f7p13d47ejsnc069ebcec164",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()['response'][0]

    return response


def getCoach(id):
    querystring = {"id":id}

    headers = {
        "X-RapidAPI-Key": "018490ae74msh76daff5b99447f7p13d47ejsnc069ebcec164",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()['response'][0]

    print(response)

getCoach(276)