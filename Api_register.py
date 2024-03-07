import requests
import json
import Dataloaders.settingloader
import Dataloaders.load_data
#from Dependencies.BypassH import bypass
import socket
import nopecha
api_url:str="https://discord.com/api/v8/auth/fingerprint"






#Constants
settings=Dataloaders.settingloader.get_settings("Data/settings.json")
user_email=settings["default_email"]
rnd_email=Dataloaders.settingloader.gen_random_email_numbers(user_email)
SITE_KEY="4c672d35-0701-42b2-88c3-78380b0db560"
USER_IP=socket.gethostbyname(socket.gethostname())
print(rnd_email)


headers = {
    'user-agent': 'Mozilla/5.0'
}
#bypass_data=bypass(sitekey=SITE_KEY,host="https://discord.com",proxy=f"{USER_IP}:5000")
#print(bypass_data)



payload = json.dumps({
       "captcha_key": None,
       "consent": True,
       "email":user_email,
       "gift_code_sku_id": None,
       "invite": "aVsMv8p2",
       "password": "MaxamusGradus",
       "username": "WhatDoesJotubMean0"
})

session = requests.Session()
r = session.post('https://discord.com/api/v9/auth/register', headers=headers,data=payload)


print(r.text)
# the session instance holds the cookie. So use it to get/post later.
# e.g. session.get('https://example.com/profile')