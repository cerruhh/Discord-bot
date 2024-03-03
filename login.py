# load all packages and scripts
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from Dataloaders.settingloader import get_settings
from Dataloaders.load_data import get_first_userdata, get_all_users
from Dataloaders.js_scripts import get_login_script

from time import sleep as wait
import json


# load settings
setting_file = get_settings("Data/settings.json")

# load constants
DEAFULT_EMAIL = setting_file["default_email"]
REGISTER_ADDRESS = "https://discord.com/login"
ACCOUNT_PATH = "Data/accounts.json"
WEBDRIVER_OPTIONS = ChromeOptions()
WEBDRIVER_OPTIONS.add_argument("--incognito")

# get account data
account_data = get_first_userdata("Data/accounts.json")
user_token = account_data["token"]

webdriver=Chrome()
webdriver.get(REGISTER_ADDRESS)
wait(0.5)


def excecute_login(webdriver, log: True):
    try:
        login_script = get_login_script(user_token)
        webdriver.execute_script(login_script)
    except KeyError or FileNotFoundError or json.JSONDecodeError:
        print("LOGIN_FAILED;ERROR NO WEBDRIVER INSERTED")


excecute_login(webdriver=webdriver,log=False)
wait(30)