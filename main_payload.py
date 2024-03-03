from Dataloaders.load_data import get_first_userdata,get_all_users
from Dataloaders.settingloader import get_settings
from login import excecute_login
from press_giveaway import enter_giveaway
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep as wait
import requests
from join_discordserver import join_discordserver



# CONSTANTS
CHROME_OPTS=ChromeOptions()
settings=get_settings(current_path="Data/settings.json")
data=get_first_userdata(c_path="Data/accounts.json")
LOGIN_ADRESS="https://discord.com/login"
test_token=data["token"]

# define webdriver
webdriver=Chrome(CHROME_OPTS)
webdriver.get(LOGIN_ADRESS)

# login to user
excecute_login(webdriver=webdriver,log=False)
print(f"loggin in with {data['user_name']}")

# join server
join_discordserver(token=test_token)



wait(30)
webdriver.quit()