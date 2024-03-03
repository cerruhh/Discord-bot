from base64 import b64encode
from json import dumps
from os import path, listdir
from random import choice
import requests
from terminut import Console
from tls_client import response
from veilcord import CaptchaSolver
from websocket import WebSocket
from Dataloaders.settingloader import get_settings

xtrack = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'


class Profile:
    def __init__(self, session, token, headers):
        self.token = token
        headers['Referer'] = 'https://discord.com/channels/@me'
        self.headers = headers
        self.ws = WebSocket()
        self.session = session

    def ConnectWS(self):
        self.ws.connect('wss://gateway.discord.gg/?encoding=json&v=9')
        self.ws.send(dumps({
            "op": 2,
            "d": {
                "token": self.token,
                "capabilities": 8189,
                "properties": {
                    "os": "Windows",
                    "browser": "Chrome",
                    "device": "",
                    "system_locale": "en-US",
                    "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                    "browser_version": "111.0.0.0",
                    "os_version": "10",
                    "referrer": "",
                    "referring_domain": "",
                    "referrer_current": "",
                    "referring_domain_current": "",
                    "release_channel": "stable",
                    "client_build_number": 199933,
                    "client_event_source": None,
                    "design_id": 0
                },
                "presence": {
                    "status": choice(["online", "idle", "dnd"]),
                    "since": 0,
                    "activities": [{
                        "name": "Custom Status",
                        "type": 4,
                        "state": "vast#1337",
                        "emoji": ""
                    }],
                    "afk": False
                },
                "compress": False,
                "client_state": {
                    "guild_versions": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": -1,
                    "private_channels_version": "0",
                    "api_code_version": 0
                }
            }
        }))

    def UpdateDOB(self) -> response.Response:
        payload = {
            "date_of_birth": "2000-05-18", "global_name": "\x4D\x41\x44\x45\x20\x42\x59\x20\x56\x41\x53\x54"
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        dobres = self.session.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload)
        return dobres

    def AddBio(self, custom_bio: str = None) -> response.Response:
        payload = {
            "bio": "discord.gg/vast" if custom_bio is None else custom_bio
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        biores = self.session.patch('https://discord.com/api/v9/users/@me/profile', headers=headers, json=payload)
        return biores

    def AddPFP(self) -> response.Response:
        folder_path = "./avatars"
        image_files = [file for file in listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        if not image_files:
            print("No image files found in the folder.")
        random_image = choice(image_files)
        image_path = path.join(folder_path, random_image)

        with open(image_path, "rb") as image_file:
            encoded_string = b64encode(image_file.read())

        payload = {
            "avatar": f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        addpfp = self.session.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload)
        return addpfp

    def AddHypesquad(self) -> response.Response:
        payload = {
            'house_id': choice(['1', '2', '3'])
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        hyperes = self.session.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
        return hyperes

    def EnableDevmode(self) -> response.Response:
        payload = {
            "settings": "agIQAQ=="
        }
        headers = self.headers
        headers["content-length"] = str(len(dumps(payload)))
        devres = self.session.patch('https://discord.com/api/v9/users/@me/settings-proto/1', headers=headers,
                                    json=payload)
        return devres


def register(self) -> bool:
    try:
        xcookies, fingerprint = self.getCookies()
        cookies = {
            '__dcfduid': xcookies.get('__dcfduid'),
            '__sdcfduid': xcookies.get('__sdcfduid'),
            '__cfruid': xcookies.get('__cfruid'),
            'locale': 'en-US',
        }
        config = get_settings('/Data/settings.json')
        captcha_service = "CAPSOLVER"
        key = "CAI-B84C18E3DC8EA33F8E46E171B9E8C152"
        cap_key = CaptchaSolver(self.session, cap_key=key, service=captcha_service,site_key="4c672d35-0701-42b2-88c3-78380b0db560").solve_captcha()


        payload = {
            "consent": True,
            "fingerprint": fingerprint,
            "username": "cc_bot0",
            "captcha_key": cap_key,
            "invite": ""
        }
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'content-length': str(len(dumps(payload))),
            'Content-Type': 'application/json',
            'Origin': 'https://discord.com',
            'Referer': 'https://discord.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12.5; XBOX Build/NHG47K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36',
            'X-Fingerprint': fingerprint,
            'X-Track': xtrack,
        }

        response = self.session.post('https://discord.com/api/v9/auth/register', headers=headers, cookies=cookies,
                                     json=payload)
        if "token" not in response.text:
            if "retry_after" in response.text:
                Console.printf(f"(-) RateLimit: {response.json().get('retry_after')}")
                return False
            Console.printf(f"(-) Failed to gen: {response.text}")
            return False

        token = response.json().get('token')

        headers.pop('content-length')
        headers.pop('X-Fingerprint')
        headers['Authorization'] = token
        status = requests.get('https://discord.com/api/v9/users/@me/library', headers=headers)
        if status.status_code != 200:
            Console.printf(f"(-) Locked Token: {token} [{status.status_code}]")
            # Stats.locked += 1
            with open("./locked.txt", "a+") as f:
                f.write(f"{token}\n")
            return False

        Console.printf(f"(+) {token}")
        # Stats.unlocked += 1
        with open("./unlocked.txt", "a+") as f:
            f.write(f"{token}\n")

        profile = Profile(self.session, token, headers)
        profile.ConnectWS()
        profile.UpdateDOB()

        humanizer = "(*) HUMANIZED | ("
        biores = profile.AddBio()
        if biores.status_code == 200:
            humanizer += "BIO"

        hyperes = profile.AddHypesquad()
        if hyperes.status_code == 204:
            humanizer += ", "
            humanizer += "HYPE"
        # enable dev mode
        devres = profile.EnableDevmode()
        if devres.status_code == 200:
            humanizer += ", "
            humanizer += "DEVMODE"

        pfpres = profile.AddPFP()
        if pfpres.status_code == 200:
            humanizer += ", "
            humanizer += "PFP"

        print(humanizer)

        return True
    except Exception as e:
        Console.printf(f"(!) ExC: {e}")


register()