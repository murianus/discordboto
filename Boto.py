import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hey Furry')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$hey':
        await client.send_message(message.channel,'Fuck off furry')
    if message.content == '$xd':
        em = discord.Embed(description='Furry')
        em.set_image(url='https://i.imgur.com/Tp9mt8B.jpg')
        await client.send_message(message.channel, embed=em)


@client.event
async def on_message(message):
    if message.content.startswith('$coin'):
        randomlist = ['!FurryCoin','69FurryCoins','0FurryCoins','324FurryCoins','26FurryCoins','900FurryCoins']
        await client.send_message(message.channel,(random.choice(randomlist)))

client.run('NTQyNzc4MDY5MDEwNzQzMzE3.Dz3C3g.ZWJuIuldonhdu3K3rb1hXdEteWk')

