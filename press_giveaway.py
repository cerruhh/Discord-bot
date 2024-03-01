import requests
from Dataloaders.settingloader import get_settings
from Dataloaders.load_data import get_all_users, get_first_userdata
from tls_client import Session,response

# get_settings
settings=get_settings("Data/settings.json")
user_data=get_first_userdata("Data/accounts.json")
user_token=user_data["token"]
DEAFULT_EMAIL=settings["default_email"]

# set up constants
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
BUTTON_REQUEST_API="https://discord.com/api/v9/interactions"



def enter_giveaway(msg_id:int,custom_id:str):
    payload = {
        'message_id': msg_id,
        'data': {'component_type': 2, 'custom_id': "page_end"}
    }
    new_session=Session(client_identifier="chrome_120",random_tls_extension_order=True)
    dev_res=Session.patch(url=BUTTON_REQUEST_API,headers=HEADERS,json=payload)
    return dev_res



