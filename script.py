import requests

listMsg = [
    "Hello!",
    "Hi",
    "What's up?"
]

#message
payload = {
    'content' : 's'
}

#autorisation discord
header = {
    'authorization' : 'token'
}

r = requests.post("discordchannel", data=payload, headers=header)