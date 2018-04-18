import random
import asyncio
import aiohttp
import requests
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!", "?")
TOKEN = "NDM1NDI1OTAzNzIwMjY3Nzc2.DbYxyA.YNl24PI0L53X7ifR1xyjxqGzCOI"

client = Bot(command_prefix=BOT_PREFIX)
        


#bot commands for net
@client.command()
async def gn():
    url = 'http://tradewinds.io/api/bots/1/lobby'
    response = requests.get(url)
    value = response.json()['gameName']
    await client.say(value)


@client.command()
async def spots():
    url = 'http://tradewinds.io/api/bots/1/lobby'
    response = requests.get(url)
    taken = response.json()['slotsTaken']
    total = response.json()['slotsTotal']
    value = int(total)-int(taken)
    await client.say("There are " + str(value) + " spots left")


@client.command()
async def stats(arg):
    player = str(arg)
    url = 'https://tradewinds.io/api/player/' + player
    if (str(requests.get(url).status_code) is '404'):
        await client.say("Player not found")
    else:
        response = requests.get(url)
        winrate = "{0:.2f}".format((int(response.json()['gamesWon'])/float(response.json()['gamesPlayed']))*100)
        stayrate = "{0:.2f}".format(100-float(response.json()['totalLeftPercent']))
        gamesplayed = response.json()['gamesPlayed']
        await client.say("Player: " + player + ". Games played: " + gamesplayed + ". Winrate: "+ str(winrate) +"%. Stayrate: " + str(stayrate) + "%.")



@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with your mom"))
    print("Logged in as " + client.user.name)


    
client.run(TOKEN)
