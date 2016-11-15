# author: Tyler Mills

import requests
import json

# add user name and password
username = ''
password = ''

# monitor you want to get data from
monitor = '3735007902'

# date range
start = "2015-01-01"
end = "2020-01-01"

endpoint = 'https://api.crimsonhexagon.com/api/'

def auth():

	auth = ''

    url = endpoint + "authenticate"

    querystring = {
        "username":username,
        "password":password,
        "noExpiration":"true"
    }

    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)

    auth = response.get('auth')

def crimson():

    url = "https://api.crimsonhexagon.com/api/monitor/posts"

    querystring = {
        "auth":auth ,
        "id":monitor,
        "start":start,
        "end":end,
        "filter":"",
        "extendLimit":"false",
        "fullContents":"true",
        "geotagged":"true"
    }

    response = requests.request("GET", url, params=querystring)

    print(response.text)

#generate authentication token
auth()

#make request
crimson()