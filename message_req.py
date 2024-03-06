import requests
import Dataloaders.settingloader
import Dataloaders.load_data
CHANNEL_ID="1213870975708430378"
TEST_MSG="HelloTHISISNOTAUTO"
def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    print(r.status_code)


def createDmChannel(token, user_id):
    data = {"recipient_id": user_id}
    headers = {"authorization": token}

    r = requests.post(f'https://discord.com/api/v9/users/@me/channels', json=data, headers=headers)
    print(r.status_code)

    channel_id = r.json()['id']

    return channel_id




# Change these variables


sendMessage(Dataloaders.load_data.get_first_userdata("Data/accounts.json")["token"], CHANNEL_ID, TEST_MSG)