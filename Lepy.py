 #-*- coding: utf-8 -*- 

clientId = "869131069616693258"
sec = 'BchRtORdte3rwbxWKfSBQBvgAxksagFi'
botToken = "ODY5MTMxMDY5NjE2NjkzMjU4.YP5vYg.peN5_cHx_9WdjudJRGMO7ag6Abw"

botName = "Lepy"
botDescription = "Python 연습용 봇입니다."

#====================================================================================================#

from typing import Coroutine
from bs4.element import ResultSet
import discord
import time
from discord import message
from discord.client import Client
from discord.embeds import Embed
from discord.ext import commands
import discord.message
import requests
from bs4 import BeautifulSoup
import json
import re
import asyncio
import random
import skill

app = commands.Bot(command_prefix='!',  help_command=None)

 
#로그인
@app.event
async def on_ready():
    print(discord.version_info)
    print('로그인을 시도합니다 : ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)
     
#강제종료
@app.command()
async def shutdown(ctx):
    await ctx.bot.logout()

#-------------------------------skill----------------------------------#

#에코
@app.command(aliases=['에코'])
async def echo(ctx, *text):
    await skill.echo(ctx, *text)
    
@echo.error
async def echo_error(ctx, error):
    await ctx.send("에러가 발생했습니다.")
    print(error)


#타이머
@app.command(aliases=['타이머'])
async def timer(ctx, num):
    await skill.timer(ctx, num)
    
            
#사칙연산
@app.command(aliases=['연산'])
async def math(ctx, *num):
    await skill.math(ctx, *num)


#DM
@app.command(aliases=['안녕'])
async def hi(ctx):
    await skill.dm(ctx)


#알람
@app.command(aliases=['알람'])
async def alram(ctx, *time):
    await skill.alram(ctx, *time)


#반응대기(홀짝)
@app.command(aliases=['홀짝'])
async def rand(ctx):
    await skill.rand(ctx)


app.run(botToken)