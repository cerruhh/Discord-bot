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

print("initializing script")
def gen_random():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)).replace("u","nx")


def gen_name():
    with open(file="Data/names.txt",mode="r",newline=None,encoding="UTF-8") as txtfile:
        c=[i.replace("\n","").replace(" ","") for i in txtfile.readlines()]
        return random.choice(c)
print("initializing complete")
print("settings flags")

ch_options=ChromeOptions()
ch_options.add_argument("--disable-blink-features=AutomationControlled")
ch_options.add_experimental_option("excludeSwitches", ["enable-automation"])
ch_options.add_experimental_option("useAutomationExtension", False)
ch_options.add_argument("--disable-gpu")
ch_options.add_argument("--disable-gpu")
ch_options.add_argument('--no-sandbox')
ch_options.add_argument('--single-process')
ch_options.add_argument('--disable-dev-shm-usage')
print("... Done")


# ch_options.add_argument("--headless")
# ch_options.add_argument("--incognito")
print("running chrome")
webdriver=Chrome(options=ch_options)
print("running navigatorFlag")
webdriver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
print("... Done")
print("Getting Website")
webdriver.get("https://discord.com/register")
print("... Got")

def join_server(server_invite: str):
    webdriver.find_element(by=By.CLASS_NAME,value="circleIconButton_d8df29").click()


wait(4)

print("Website loaded!")
print("Getting Elements")
email_box = webdriver.find_element(by=By.NAME, value="email")
password_box=webdriver.find_element(by=By.NAME,value="password")
username=webdriver.find_element(by=By.NAME,value="username")
displayname=webdriver.find_element(by=By.NAME,value="global_name")
check_box=webdriver.find_elements(by=By.CLASS_NAME,value="input__52838")[1]

print("Creating Dummmy Credentials")
TEMP_INVITE="WzUmVnEeEr"
d_name=gen_name()
emailsplit=get_email_split(setting_file['default_email'])
e_name=f"{emailsplit[0]}+{gen_random()}@{emailsplit[1]}"
print(f"EMAIL: {e_name}")
u_name=d_name+str(random.randint(0,1928685))
print(f"USERNAME: {u_name}")
p_pass=gen_random()
print(p_pass)

print("... Done")

print("Sending Credentials")
email_box.send_keys(e_name)
password_box.send_keys(p_pass)
displayname.send_keys(d_name)
username.send_keys(u_name)

print("... Done")

print("Checking:")
check_box.click()
password_box.click()

print("Setting Birth")
day=webdriver.find_element(by=By.CLASS_NAME,value="day__86dab").find_element(by=By.CLASS_NAME,value="css-1hwfws3")
month=webdriver.find_element(by=By.CLASS_NAME,value="month_c81b3d").find_element(by=By.CLASS_NAME,value="css-1hwfws3")
year=webdriver.find_element(by=By.CLASS_NAME,value="css-1hwfws3")

login_box=webdriver.find_element(by=By.CLASS_NAME,value="button__5573c")

#
action=ActionChains(webdriver)
action.send_keys(Keys.TAB).perform()
print("birth Keys")
for _ in range(0,3):
    action.send_keys(Keys.UP).perform()
    action.send_keys(Keys.ENTER).perform()

# alexander_stubb=webdriver.find_element(by=By.CLASS_NAME,value="css-3esr4u-a11yText")
# alexander_stubb.click()
print("Registering... Please input hCaptcha to proceed")
login_box.click()
if str(input("Done with captcha (press E to abort!)?: "))=="E":
    exit(0)

storage=LocalStorage(webdriver)
webdriver.refresh()
wait(0.2)





wait(3)


wait(200)

webdriver.quit()