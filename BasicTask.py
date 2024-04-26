from undetected_chromedriver import Chrome
from undetected_chromedriver import ChromeOptions

def CreateDriver():
    ch_options=ChromeOptions()

    ch_options.add_argument("--disable-blink-features=AutomationControlled")
    #ch_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #ch_options.add_experimental_option("useAutomationExtension", False)
    ch_options.add_argument("--disable-gpu")
    ch_options.add_argument("--disable-gpu")
    ch_options.add_argument('--no-sandbox')
    ch_options.add_argument('--single-process')
    ch_options.add_argument('--disable-dev-shm-usage')

    driver=Chrome(options=ch_options)
    driver.set_page_load_timeout(50)
    driver.implicitly_wait(50)

    return driver