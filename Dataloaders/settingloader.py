import json
from os.path import abspath



def get_settings(current_path:str):
    with open(file=current_path,mode="r",encoding="UTF-8") as settingfile:
        json_data=json.load(settingfile)
        return json_data["settings"]


def get_email_split(email:str):
    return email.split("@")