import copy
import json
import pathlib
import re

import requests
from bs4 import BeautifulSoup
from lxml import html

default_userdata_path = pathlib.Path("./confidential/userdata.json")

if default_userdata_path.exists():
    userdata_json = json.load(open(default_userdata_path, 'r'))
else:
    print("Error: userdataが存在しません")
    exit(1)

fid = userdata_json["fightersid"]

url = "https://game.capcom.com/cfn/sfv/profile/" + fid

session = requests.session()

cookie = ""
for key in userdata_json["cookie"]:
    cookie += key + "=" + userdata_json["cookie"][key] + "; "

response = session.get(url, headers={"Cookie": cookie})

soup = BeautifulSoup(response.text, "html.parser")

lxml_converted_data = html.fromstring(str(soup))

league_points = lxml_converted_data.xpath(
    '/html/body/div[1]/main/section[2]\
        /div/div[2]/div[4]/div/div[1]/dl[2]/dd/text()')[0]
wins = lxml_converted_data.xpath(
    '/html/body/div[1]/main/section[3]\
        /div/ul[2]/li[1]/div[3]/dl[2]/dd')[0].text
loses = lxml_converted_data.xpath(
    '/html/body/div[1]/main/section[3]\
        /div/ul[2]/li[1]/div[3]/dl[3]/dd')[0].text

if league_points == "" or wins == "" or loses == "":
    print("Error: Can't get Wins or Loses or LeaguePoint")
    exit(1)

print("league_points:", league_points)
print("wins:", wins)
print("loses:", loses)

next_userdata_json = copy.deepcopy(userdata_json)

next_userdata_json["LeaguePoints"] = league_points
next_userdata_json["Wins"] = wins
next_userdata_json["Loses"] = loses

set_cookie = re.split(r'[,;] ', response.headers['Set-Cookie'])

target = ["scirid", "fuel_csrf_token"]
for pram in set_cookie:
    for s in target:
        if (re.match(s, pram)):
            key, val = pram.split("=")
            next_userdata_json["cookie"][key] = val

scirid = userdata_json["cookie"]["scirid"]
fuel_csrf_token = userdata_json["cookie"]["fuel_csrf_token"]
next_scirid = next_userdata_json["cookie"]["scirid"]
next_fuel_csrf_token = next_userdata_json["cookie"]["fuel_csrf_token"]

if next_scirid != scirid and next_fuel_csrf_token != fuel_csrf_token:
    with open(default_userdata_path, "w") as f:
        json.dump(next_userdata_json, f, indent=4)
