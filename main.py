from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep as wait
import random
import string
import json



def gen_random():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

def gen_name():
    with open(file="Data/lol.txt",mode="r",newline=None,encoding="UTF-8") as txtfile:
        c=[i.replace("\n","").replace(" ","") for i in txtfile.readlines()]
        return random.choice(c)


ch_options=ChromeOptions()
#ch_options.add_argument("--headless")

webdriver=Chrome(ch_options)
webdriver.get("https://discord.com/register")


def join_server(server_invite: str):
    webdriver.find_element(by=By.CLASS_NAME,value="circleIconButton_d8df29").click()

wait(3)
email_box = webdriver.find_element(by=By.NAME, value="email")
password_box=webdriver.find_element(by=By.ID,value="uid_8")
username=webdriver.find_element(by=By.ID,value="uid_7")
displayname=webdriver.find_element(by=By.ID,value="uid_6")
check_box=webdriver.find_elements(by=By.CLASS_NAME,value="inputDefault__7fb3f")[1]


d_name=gen_name()+str(random.randint(0,1928685))
e_name=f"nutchy.toadish+{gen_random()}@gmail.com"
u_name=gen_name()+str(random.randint(0,1928685))
p_pass=gen_random()

email_box.send_keys(e_name)
password_box.send_keys(p_pass)
displayname.send_keys(d_name)
username.send_keys(u_name)
with open(file="Data/accounts.json",mode="r+") as file:
    json_load=json.load(file)
    print(json_load)
    json_load=json_load["accounts"][u_name]={
        "display_name": d_name,
        "pass": p_pass,
        "email": e_name,
        "username": u_name
    }
    json.dump(obj=json_load,fp=file)


check_box.click()
password_box.click()

day=webdriver.find_element(by=By.CLASS_NAME,value="day__86dab").find_element(by=By.CLASS_NAME,value="css-1hwfws3")
month=webdriver.find_element(by=By.CLASS_NAME,value="month_c81b3d").find_element(by=By.CLASS_NAME,value="css-1hwfws3")
year=webdriver.find_element(by=By.CLASS_NAME,value="css-1hwfws3")

login_box=webdriver.find_element(by=By.CLASS_NAME,value="button__47891")


action=ActionChains(webdriver)
action.send_keys(Keys.TAB).perform()
for _ in range(0,3):
    action.send_keys(Keys.UP).perform()
    action.send_keys(Keys.ENTER).perform()

# alexander_stubb=webdriver.find_element(by=By.CLASS_NAME,value="css-3esr4u-a11yText")
# alexander_stubb.click()
login_box.click()
wait(30)
action.send_keys(Keys.ESCAPE).perform()
for _ in range(0,10):
    action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.ENTER).perform()

#join_server("JPEXgqSq")
wait(10)

webdriver.quit()