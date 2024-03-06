from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep as wait
from Dataloaders.settingloader import get_settings
from Dataloaders.settingloader import get_email_split
from Dataloaders.LocalStorage import LocalStorage
import random
import string

setting_file=get_settings("Data/settings.json")


def gen_random():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)).replace("u","nx")


def gen_name():
    with open(file="Data/lol.txt",mode="r",newline=None,encoding="UTF-8") as txtfile:
        c=[i.replace("\n","").replace(" ","") for i in txtfile.readlines()]
        return random.choice(c)


ch_options=ChromeOptions()
# ch_options.add_argument("--headless")
# ch_options.add_argument("--incognito")

webdriver=Chrome(ch_options)
webdriver.get("https://discord.com/register")


def join_server(server_invite: str):
    webdriver.find_element(by=By.CLASS_NAME,value="circleIconButton_d8df29").click()


wait(4)


email_box = webdriver.find_element(by=By.NAME, value="email")
password_box=webdriver.find_element(by=By.NAME,value="password")
username=webdriver.find_element(by=By.NAME,value="username")
displayname=webdriver.find_element(by=By.NAME,value="global_name")
check_box=webdriver.find_elements(by=By.CLASS_NAME,value="inputDefault__7fb3f")[1]

TEMP_INVITE="WzUmVnEeEr"
d_name=gen_name()+str(random.randint(0,1928685))
emailsplit=get_email_split(setting_file['default_email'])
e_name=f"{emailsplit[0]}+{gen_random()}@{emailsplit[1]}"
print(e_name)
u_name=gen_name()+str(random.randint(0,1928685))
p_pass=gen_random()

email_box.send_keys(e_name)
password_box.send_keys(p_pass)
displayname.send_keys(d_name)
username.send_keys(u_name)
# with open(file="Data/accounts_old.json",mode="r+") as file:
#
#     json_load=json.load(file)
#     file.truncate(0)
#     print(file.read())
#     print(json_load)
#     json_load["accounts"][u_name]={
#         "display_name": d_name,
#         "pass": p_pass,
#         "email": e_name,
#         "username": u_name
#     }
#     json.dump(json_load,file)


check_box.click()
password_box.click()

day=webdriver.find_element(by=By.CLASS_NAME,value="day__86dab").find_element(by=By.CLASS_NAME,value="css-1hwfws3")
month=webdriver.find_element(by=By.CLASS_NAME,value="month_c81b3d").find_element(by=By.CLASS_NAME,value="css-1hwfws3")
year=webdriver.find_element(by=By.CLASS_NAME,value="css-1hwfws3")

login_box=webdriver.find_element(by=By.CLASS_NAME,value="button__47891")

#
action=ActionChains(webdriver)
action.send_keys(Keys.TAB).perform()
for _ in range(0,3):
    action.send_keys(Keys.UP).perform()
    action.send_keys(Keys.ENTER).perform()

# alexander_stubb=webdriver.find_element(by=By.CLASS_NAME,value="css-3esr4u-a11yText")
# alexander_stubb.click()
login_box.click()
if str(input("rdy?: "))=="E":
    exit(0)

storage=LocalStorage(webdriver)
webdriver.refresh()
print(storage.keys())
got_token=storage.get("token")
print(got_token)
print(username)



wait(3)

# action.send_keys(Keys.ESCAPE).perform()
# webdriver.find_element(by=By.XPATH,value='//*[@id="app-mount"]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[2]/a').click() #want to join a server?
# wait(0.1)
# action.send_keys(Keys.TAB).perform()
# action.send_keys(TEMP_INVITE).perform()
# wait(0.1)
# webdriver.find_element(by=By.XPATH,value='//*[@id="app-mount"]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[2]/button[1]').click() #join


wait(200)

webdriver.quit()