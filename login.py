from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep as wait
import random
import string
import json



DEAFULT_EMAIL="uburner.adam@gmail.com"
REGISTER_ADDRESS="https://discord.com/login"
ACCOUNT_PATH="Data/accounts.json"
WEBDRIVER_OPTIONS=ChromeOptions()
WEBDRIVER_OPTIONS.add_argument("--incognito")

EMAIL_NAME="email"

with open(file=ACCOUNT_PATH,mode="r",newline=None,encoding="UTF-8") as json_file:
    account_data=json.load(json_file)
    account_data=account_data["accounts"]

discord_webdriver=Chrome(WEBDRIVER_OPTIONS)
discord_webdriver.get(url=REGISTER_ADDRESS)
wait(3)
#discord_webdriver.find_element(by=By.NAME,value=EMAIL_NAME).send_keys(account_data["RamonRobbins1507940"][EMAIL_NAME])

actions=ActionChains(discord_webdriver)
#
# actions.send_keys(Keys.TAB).perform()
#
# actions.send_keys(account_data["RamonRobbins1507940"]["display_name"]).perform()
# actions.send_keys(Keys.TAB).perform()
# actions.send_keys(account_data["RamonRobbins1507940"]["username"]).perform()
# actions.send_keys(Keys.TAB).perform()
# actions.send_keys(account_data["RamonRobbins1507940"]["pass"]).perform()
# for _ in range(7):
#     actions.send_keys(Keys.UP).perform()
#     actions.send_keys(Keys.ENTER).perform()
# actions.send_keys(Keys.TAB).perform()
# actions.send_keys(Keys.TAB).perform()
# actions.send_keys(Keys.TAB)
# actions.send_keys(Keys.SPACE).perform()
# actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).perform()
# actions.key_up(Keys.SHIFT)
#
# actions.send_keys(Keys.TAB).perform()
# actions.send_keys(Keys.SPACE).perform()


discord_webdriver.find_element(by=By.NAME,value=EMAIL_NAME).send_keys(account_data["RamonRobbins1507940"][EMAIL_NAME])

discord_webdriver.find_element(by=By.NAME,value="password").send_keys(account_data["RamonRobbins1507940"]["pass"])

actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.SPACE).perform()
wait(30)

# wait(4)









# def forTabs(n:int,webdriver):
#     for _, in range(0,n):
#


