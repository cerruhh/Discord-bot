from Dataloaders.load_data import get_first_userdata,get_all_users
from Dataloaders.settingloader import get_settings
from login import excecute_login
from press_giveaway import enter_giveaway
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

# CONSTANTS
CHROME_OPTS=ChromeOptions()
settings=get_settings(current_path="Data/settings.json")
data=get_first_userdata(c_path="Data/accounts.json")


# define webdriver
webdriver=Chrome(CHROME_OPTS)


