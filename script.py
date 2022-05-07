import requests
#import time

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
discordchannel = input("Enter the link of the discord channel:")

r = requests.post(discordchannel, data=payload, headers=header)

### LOOP ###

#while(True):
#    print('test')
#    time.sleep(5)