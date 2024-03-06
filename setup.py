import json
import os
from time import sleep as wait
from Dataloaders.settingloader import change_setting

NAME = 'discord beef.'
DESCRIPTION = 'A bot that automatically can win giveaways'
URL = 'https://github.com/cerruhh/Discord-bot/'
EMAIL = 'uadam.burner@gmail.com'
AUTHOR = 'Cerruhh'
REQUIRES_PYTHON = '>=2.7.0'
VERSION = '0.0.1'

REQUIRED = [
    'requests',
    'requests_toolbelt',
    'brotli',
    'filetype',
    'websocket-client==0.59.0',
    'ua-parser',
    'colorama',
    'selenium'
]

account_template={
  "account_list":[

  ]
}

setting_template={
  "settings": {
    "default_email": ""
  }
}

try:
    with open(file="Data/accounts.json",mode="r") as file:
        f=file.read()

except FileNotFoundError or json.JSONDecodeError:
    print("Setting up project!")
    os.mkdir("Data")
    print("Creating Data folder!")
    wait(0.1)
    with open(file="Data/accounts.json",mode="r+") as file:
        print("Creating account file!")
        json.dump(account_template,file)
    print("Completed account file creation!")

    with open(file="Data/settings.json",mode="r+") as file:
        print("Creating setting file!")
        setting_template_clone=setting_template
        deafult_email=input("What is ur email? (please, do not use your personal email for this bot!)")

        json.dump(account_template,file)

else:
    answer=input("Setup was not needed! Run main_payload.py to run program or would you like to change deafult email? Y/N ")
    if answer.lower()=="n":
        exit(-9)
    else:
        new_email=input("What is ur new email? (please do not use your main email for this!) ")
        change_setting(key="default_email",value=new_email,path="Data/settings.json")