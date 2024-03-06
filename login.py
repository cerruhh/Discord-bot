# load all packages and scripts
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from Dataloaders.settingloader import get_settings
from Dataloaders.load_data import get_first_userdata, get_all_users
from Dataloaders.js_scripts import get_login_script
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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
#
# webdriver=Chrome()
# webdriver.get(REGISTER_ADDRESS)
# wait(0.5)


def excecute_login(webdriver, log: True):
    try:
        login_script = get_login_script(user_token)
        webdriver.execute_script(login_script)
    except KeyError or FileNotFoundError or json.JSONDecodeError:
        print("LOGIN_FAILED;ERROR NO WEBDRIVER INSERTED")


def execute_join(webdriver,invite:str): #6
    actions = ActionChains(webdriver) #7
    for i in range(0,7):
        actions.send_keys(Keys.TAB).perform()
    wait(0.3)
    actions.send_keys(Keys.ENTER).perform()
    wait(0.4)
    join_server_button=webdriver.find_element(by=By.XPATH,value='//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/nav/ul/div[2]/div[4]/div[1]/div/div/svg/foreignObject/div')
    join_server_button.click()
    wait(0.3)
    input_box=webdriver.find_element(by=By.CSS_SELECTOR,value='[placeholder="https://discord.gg/hTKzmak"]')
    input_box.click()
    input_box.send_keys(invite)
    wait(0.3)

    for i in range(0,6): #6 times
        actions.send_keys(Keys.TAB).perform()
        wait(0.05)
    wait(10)
    actions.send_keys(Keys.ENTER).perform()
    wait(30)

