from Dataloaders.load_data import get_first_userdata
from Dataloaders.settingloader import get_settings
from login import excecute_login,execute_join
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep as wait
import join_discordserver

# CONSTANTS
CHROME_OPTS=ChromeOptions()
settings=get_settings(current_path="Data/settings.json")
data=get_first_userdata(c_path="Data/accounts.json")
LOGIN_ADRESS="https://discord.com/login"
test_token=data["token"]
LOCATION="join guild"

# define webdriver
webdriver=Chrome(CHROME_OPTS)
webdriver.get(LOGIN_ADRESS)

# login to user
excecute_login(webdriver=webdriver,log=False)
wait(10)
execute_join(webdriver=webdriver,invite="krunker")
wait(30)
print(f"loggin in with {data['user_name']}")

# join server
#join_discordserver.joinGuild(location=LOCATION,inviteCode="WzUmVnEeEr",guild_id="1213870975217836084",wait_time=0.5)

# send messahe

wait(30)
webdriver.quit()