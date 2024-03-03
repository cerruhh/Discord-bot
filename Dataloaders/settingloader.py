import json



def get_settings(current_path:str):
    with open(file=current_path,mode="r",encoding="UTF-8") as settingfile:
        json_data=json.load(settingfile)
        return json_data["settings"]


def get_email_split(email:str):
    return email.split("@")

def change_setting(key:str,value,path:str):
    with open(file=path,mode="r+") as setting_file:
        load_json=json.load(setting_file)
        load_json["settings"][key]=value
        setting_file.truncate(0)
        setting_file.seek(0)
        json.dump(load_json,setting_file,indent=1)

