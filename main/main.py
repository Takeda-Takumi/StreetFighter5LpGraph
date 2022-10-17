import json
import pathlib

default_userdata_path = pathlib.Path("./confidential/userdata.json")

if default_userdata_path.exists():
    userdata_json = json.load(open(default_userdata_path, 'r'))
else:
    print("Error: userdataが存在しません")
    exit(0)

cookie = userdata_json["cookie"]
