# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:10:10 2018

@author: TripleQuestionMark
"""

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event #when something happens in client,this triggered
async def on_ready():
    print("The Lord has gifted you a ready bot boy")

@client.event
async def on_message(message):
    
    if message.content.lower() == "i love satan" or message.content.lower() == "i love the devil" or message.content.lower() == "i am gay" or message.content.lower() == "im gay" or message.content.lower() == "i'm gay": #if someone says no u
        await client.send_message(message.channel, "Banned.") #then reply "no u" back in the same channel

    if message.content.lower() == "no u" and message.author.bot == False:
        await client.send_message(message.channel, "no u")
    
    if message.content.lower() == "amen" or message.content.lower() == "amen.": 
        await client.send_message(message.channel, "Amen :pray:")
        
    if " fag" in message.content.lower() and message.author.bot == False:
        await client.send_message(message.channel, message.author.mention + " is the biggest fag")
        

client.run("NDE3MTY0MTY1MDE5NDY3Nzc2.DXPUbg.E3dbdvyTIySwVFCvk2Silxk4Spw")
