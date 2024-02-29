from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from settingloader import get_settings
from time import sleep as wait
import random
import string
import json

setting_file=get_settings()


DEAFULT_EMAIL=setting_file["default_email"]
REGISTER_ADDRESS="https://discord.com/login"
ACCOUNT_PATH= "Data/accounts.json"
WEBDRIVER_OPTIONS=ChromeOptions()
# WEBDRIVER_OPTIONS.add_argument("--incognito")

with open(file=ACCOUNT_PATH,mode="r",newline=None,encoding="UTF-8") as json_file:
    account_data=json.load(json_file)
    print(account_data)
    account_data=account_data["account_list"]

discord_webdriver=Chrome(WEBDRIVER_OPTIONS)
discord_webdriver.get(url=REGISTER_ADDRESS)
user_token=account_data[0]["token"]
wait(4)
print("""
    function login(token) {
    setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
    location.reload();
    }, 2500);
    }
    
    login('"""+user_token+"""')
""")
discord_webdriver.execute_script("""
    function login(token) {
    setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
    location.reload();
    }, 2500);
    }
    
    login('"""+user_token+""""')
""")
wait(10)
discord_webdriver.refresh()

wait(10)

discord_webdriver.quit()









wait(3)










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


# discord_webdriver.find_element(by=By.NAME,value=EMAIL_NAME).send_keys(account_data["RamonRobbins1507940"][EMAIL_NAME])
#
# discord_webdriver.find_element(by=By.NAME,value="password").send_keys(account_data["RamonRobbins1507940"]["pass"])
#
# actions.send_keys(Keys.TAB).perform()
# actions.send_keys(Keys.TAB).perform()
# actions.send_keys(Keys.SPACE).perform()
