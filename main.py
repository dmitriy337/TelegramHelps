
from telethon import TelegramClient, events, utils, types
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon import *
import datetime
import urllib.request
import json
import os
import asyncio
import time
import pyttsx3
import os
from gtts import gTTS
import random
import requests
from bs4 import BeautifulSoup as bs
import datetime

api_id = """Your Id"""
api_hash = """Your Hash"""
client = TelegramClient('anon', api_id, api_hash)
client.start()


headers = {
    'authority': 'sinoptik.ua',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.google.com/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'os=LINUX; b=b; _ga=GA1.2.1637046170.1592915677; _gid=GA1.2.1404080064.1592915677; __gads=ID=9e78e132d83e0a7e:T=1592915676:S=ALNI_MYv7u65BCvKfXIXo49-10yHps53pA; cities=303015812; location=165.100524901; cbtYmTName=CXIrYG0rMys7bT4wOms7Ozo+PG1oODk9K3R/; cbtYmTNames=[]',
    'if-none-match': '"dd477b7262cced8ce6c3b202728b94a7"',
}

#https://sinoptik.ua/ - adn your city 
def pogodasegodnia():
    pogodaa = []
    vremia = []
    nebo = []
    temperatyra = []
    response = requests.get("""Link https://sinoptik.ua/ and your city""", headers=headers)
    soup = bs(response.text, "html.parser")
    news = soup.find('table', class_='weatherDetails')
    time = news.find(class_ = 'gray time')
    times = time.findAll('td')
    for ti in times:
        vremia.append(ti.text)
    kak = news.find('tr',class_='img weatherIcoS')
    pri= kak.findAll('div')
    for pr in pri:
        nebo.append((pr.attrs['title']))
    temp = news.find('tr',class_='temperature')
    pemp = temp.findAll('td')
    trr =[]
    for pe in temp:
        if '+' in str(pe):
            p = str(pe).split('+')
            y = (p[1][:-5])
            temperatyra.append(f'+{y}')
        else:
            pass

    for i in range(0,8):
        pogodaa.append(f"Time: {vremia[i]}. Weather: {nebo[i]}. Temperatyre: {temperatyra[i]} ")
    return ('\n\n'.join(pogodaa))
    pogodaa = []
    vremia = []
    nebo = []
    temperatyra = []



def pogodazavtra():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    pogodaa = []
    vremia = []
    nebo = []
    temperatyra = []
    response = requests.get(f'  """Link https://sinoptik.ua/ and your city"""  {tomorrow}', headers=headers)
    soup = bs(response.text, "html.parser")
    news = soup.find('table', class_='weatherDetails')
    time = news.find(class_ = 'gray time')
    times = time.findAll('td')
    for ti in times:
        vremia.append(ti.text)
    kak = news.find('tr',class_='img weatherIcoS')
    pri= kak.findAll('div')
    for pr in pri:
        nebo.append((pr.attrs['title']))
    temp = news.find('tr',class_='temperature')
    pemp = temp.findAll('td')
    trr =[]
    for pe in temp:
        if '+' in str(pe):
            p = str(pe).split('+')
            y = (p[1][:-5])
            temperatyra.append(f'+{y}')
        else:
            pass

    for i in range(0,8):
        pogodaa.append(f"Time: {vremia[i]}. Weather: {nebo[i]}. Temperatyre: {temperatyra[i]} ")
    return ('\n\n'.join(pogodaa))
    pogodaa = []
    vremia = []
    nebo = []
    temperatyra = []


#Forvard photo to group
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        if 'media=MessageMediaPhoto' in str(event):
            try:
                await client.forward_messages('me',event.message)
            except Exception as e:
                print(e)
        else:
            pass


#Typing...
@client.on(events.NewMessage(pattern='(^!t$)|(^!Typing$)|(^!typing$)', outgoing=True))
async def handler(event):
    try:
        chat = await event.get_chat()
        await event.delete()
        async with client.action(chat, 'typing'):
            await asyncio.sleep(40)
            pass

    except Exception as e:
        print(e)


#Send voice
@client.on(events.NewMessage(pattern='(^!gs$)|(^!voice$)|(^!voice$)|(^!g$)', outgoing=True))
async def handler(event):
    try:
        chat = await event.get_chat()
        await event.delete()
        async with client.action(chat, 'audio'):
            await asyncio.sleep(20)
            pass

    except Exception as e:
        print(e)


#Send help message
@client.on(events.NewMessage(pattern='(^!help$)|(^!Comands$)|(^!comands$)|(^!Help$)', outgoing=True))
async def handler(event):
    try:
        await event.reply(open('help.txt', 'r').read())

    except Exception as e:
        print(e)


# Google voice 
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    message_id = event.message.chat_id
    if '!а' in str(event.message.message):
        tetx = event.message.message
        await event.delete()
        tts = gTTS(text=(tetx)[2:], lang='en',slow = False)
        tts.save('sd.mp3')
        await client.send_file(message_id, 'sd.mp3', attributes=[types.DocumentAttributeAudio( duration=random.randint(3, 60) ,voice=True, waveform=utils.encode_waveform(bytes(((random.randint(3, 60), random.randint(3, 60), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), 31, 31)) * random.randint(1, 10))))])
    elif '!a' in str(event.message.message):
        tetx = event.message.message
        await event.delete()
        tts = gTTS(text=(tetx)[2:], lang='en')
        tts.save('sd.mp3')
        await client.send_file(message_id, 'sd.mp3', attributes=[types.DocumentAttributeAudio(duration =random.randint(3, 60), voice=True, waveform=utils.encode_waveform(bytes(((random.randint(3, 60), random.randint(3, 60), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), 31, 31)) * random.randint(1, 10))))])



#Weather
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    if '!weather' in str(event.message.message).lower():
        if 'tomorrow' in str(event.message.message).lower():

            try:
               # origin_text = event.message.text.replace('!sp ', '')
                origin_text = (f'Weather Tomorrow: \n{pogodazavtra()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)
        elif 'today' in str(event.message.message).lower():

            try:
                origin_text = (f'Weather Today: \n{pogodasegodnia()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)
        else:
            try:
               # origin_text = event.message.text.replace('!sp ', '')
                origin_text = (f'Weather Today: \n{pogodasegodnia()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)
    


#Spam
@client.on(events.NewMessage(pattern='(^!spam$)|(^!sp$)', outgoing=True))
async def handler(event):
    try:
        # origin_text = event.message.text.replace('!sp ', '')
        origin_text = (open('spam.txt','r').read())
        chat = await event.get_chat()

        await event.delete()

        for i in range(3):
            await client.send_message(chat, origin_text)
            time.sleep(1)
        origin_text = '1'

    except Exception as e:
        print(e)


#Status and my life day
async def update_bio():
    while True:
        delta = ((datetime.datetime.now() - datetime.datetime(2004, 3, 22))).days
        string = f'I live already {delta} days🌮\n'

        from telethon.tl.functions.account import UpdateProfileRequest

        await client(UpdateProfileRequest(
            about=string
        ))
        await asyncio.sleep(600)

    
try:
    print('(Press Ctrl+C to stop this)')
    loop = asyncio.get_event_loop()
    task = loop.create_task(update_bio())
    loop.run_until_complete(task)

    client.run_until_disconnected()
finally:
    client.disconnect()

