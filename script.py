import requests
import time
import random

#custom rdm messages
listMsg = [
    "Hello!",
    "Hi",
    "What's up?"
]

#message
payload = {
    'content' : 'supa'
}

### INIT ###

#autorisation discord
header = {
    'authorization' : input("Enter your discord authorization token:")
}

#where to spam
discordChannel = input("Enter the link of the discord channel:")


### LOOP ###

while(True):
    wtTime = random.randint(5,10)
    time.sleep(wtTime*60) #5 to 10 minutes of wait before sending

    rd = random.randint(0,len(listMsg)-1)
    payload = {
    'content' : listMsg[rd]
    }
    requests.post(discordChannel, data=payload, headers=header)