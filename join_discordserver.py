import requests
from time import sleep as wait

from Dependencies.restAPI.RESTapiwrap import Wrapper
from Dependencies.ContextProperties.Context_Properties import ContextProperties
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote



# def join_discordserver(token:str,server_invite):
#     header={
#         "authorization":token
#     }
#     discord_request=requests.post(url=f"https://discord.com/api/v9/invites/{server_invite}",headers=header,json={})
#     print(discord_request.status_code)
#     discord_request.raise_for_status()
log={"console":True, "file":False}
discord="https://discord.com/api/v9"
s=requests.Session()
def joinGuildRaw(inviteCode, guild_id=None, channel_id=None, channel_type=None, location="join guild"):
    url = discord + "invites/" + inviteCode
    if location in ("accept invite page", "join guild"):
        return Wrapper.sendRequest(s, 'post', url, {}, headerModifications={"update": {
            "X-Context-Properties": ContextProperties.get(location, guild_id=guild_id, channel_id=channel_id,
                                                          channel_type=channel_type)}}, log=log)
    elif location == "markdown":
        return Wrapper.sendRequest(s, 'post', url, {}, headerModifications={
            "update": {"X-Context-Properties": ContextProperties.get("markdown")}}, log=log)


def getInfoFromInviteCode(inviteCode, with_counts, with_expiration, fromJoinGuildNav,session):
    url = discord + "invites/" + inviteCode
    if with_counts is not None or with_expiration is not None or fromJoinGuildNav:
        url += "?"
        data = {}
        if fromJoinGuildNav:
            data["inputValue"] = inviteCode
        if with_counts is not None:
            data["with_counts"] = with_counts
        if with_expiration is not None:
            data["with_expiration"] = with_expiration
        url += "&".join("%s=%s" % (k, quote(repr(data[k]).lower())) for k in data)
    return Wrapper.sendRequest(session, 'get', url, log=log)


def joinGuild(inviteCode, location, wait_time, guild_id):
    location = location.lower()
    if location in ("accept invite page", "join guild"):
        guildData = getInfoFromInviteCode(inviteCode=inviteCode, with_counts=True, with_expiration=True,
                                          fromJoinGuildNav=(location.lower() == "join guild"),session=s).json()
        if wait_time is not None:
            wait(wait_time)
        print(guildData)
        return joinGuildRaw(inviteCode, guild_id, guildData["channel"]["id"], guildData["channel"]["type"], location)
