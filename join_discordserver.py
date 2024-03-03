import requests

def join_discordserver(token:str,server_invite):
    header={
        "authorization":token
    }
    discord_request=requests.post(url="https://discord.com/api/v8/invites/{}".format(server_invite),headers=header)
    discord_request.raise_for_status()
