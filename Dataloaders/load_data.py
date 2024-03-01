import json


def get_first_userdata(c_path:str) -> dict:
    with open(file=c_path, encoding="UTF-8", newline=None) as file:
        json_load=json.load(file)
        return json_load["account_list"][0]


def get_all_users(c_path:str) -> dict:
    with open(file=c_path, encoding="UTF-8", newline=None) as file:
        json_load=json.load(file)
        return json_load["account_list"]