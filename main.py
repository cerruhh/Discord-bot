from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep as wait
import random
import string

def gen_random():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

ch_options = ChromeOptions()
#ch_options.add_argument("--headless")

webdriver=Chrome(ch_options)
webdriver.get("https://discord.com/register")

wait(3)
email_box = webdriver.find_element(by=By.NAME, value="email")
password_box=webdriver.find_element(by=By.ID,value="uid_8")
username=webdriver.find_element(by=By.ID,value="uid_7")
displayname=webdriver.find_element(by=By.ID,value="uid_6")
check_box=webdriver.find_elements(by=By.CLASS_NAME,value="inputDefault__7fb3f")[1]

email_box.send_keys(f"nutchy.toadish+{gen_random()}@gmail.com")
password_box.send_keys(gen_random())
displayname.send_keys(gen_random())
username.send_keys(gen_random())

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
wait(15)

webdriver.quit()