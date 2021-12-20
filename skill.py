import random
import time
from discord import message
from discord.client import Client
from discord.embeds import Embed
from discord.ext import commands
import discord.message
import asyncio
import re
import os

app = commands.Bot(command_prefix='!',  help_command=None)


# dm
async def dm(ctx):
    dm_channel = await ctx.message.author.create_dm()
    await dm_channel.send(f'{ctx.message.author.mention}님, 나도 안녕!')

# 에코
async def echo(ctx, *text):
    txt = ''
    if len(text) == 0:
        await ctx.send('echo result')
    else :
        for tmp in text:
            txt = txt + tmp
            txt += ', '
        await ctx.send('echo : ' +txt[:-2])

# 타이머
async def timer(ctx, num):
    num = int(num)
    t = time.strftime('%S')
    while num > 0:
        if t != time.strftime('%S'):
            await ctx.send(num)
            num -= 1
            t = time.strftime('%S')

# 연산
async def math(ctx, *num):
    number = []
    total = 0

    for i in range(len(num)):
        number.append(num[i])

    for i in range(len(number)):
        if number[i] == "*":
            number[i+1] = float(number[i-1]) * float(number[i+1])
            number[i-1] = 0
            number[i] = 0

        if number[i] == "/":
            number[i+1] = float(number[i-1]) / float(number[i+1])
            number[i-1] = 0
            number[i] = 0

    for i in range(len(number)):
        if number[i] == "+":
            number[i+1] =  float(number[i-1]) + float(number[i+1])
            number[i-1] = 0
            number[i] = 0

        if number[i] == "-":
            number[i+1] =  float(number[i-1]) - float(number[i+1])
            number[i-1] = 0
            number[i] = 0

    for i in range(0,len(number),2):
        total = float(total) + float(number[i])

    await ctx.send(total)

# 알람
async def alram(ctx, *time):
    t_hour = re.compile('(?P<hour>\d+)시간')
    t_min = re.compile('(?P<min>\d+)분')
    t_sec = re.compile('(?P<sec>\d+)초')

    hour, min, sec = 0, 0, 0

    for i in time:
        try:
            reg_h = t_hour.search(i)
            t_hour = reg_h.group('hour')
            if t_hour != None:
                hour = int(t_hour)
        except: pass

        try:
            reg_m = t_min.search(i)
            t_min = reg_m.group('min')
            if t_min != None:
                min = int(t_min)
        except: pass

        try:
            reg_s = t_sec.search(i)
            t_sec = reg_s.group('sec')
            if t_sec != None:
                sec = int(t_sec)
        except: pass

    context = f'{ctx.message.author}님의 알람 설정'
    content = ""
    if hour > 0:
        content += f"{hour}시간 "
    if min > 0:
        content += f"{min}분 "
    if sec > 0:
        content += f"{sec}초 "
    content += "뒤에 DM을 보내드릴게요!"

    embed_1 = discord.Embed(title=context, description=content, color = 0xCC99FF)
    await ctx.send(embed=embed_1)

    await asyncio.sleep(hour * 3600 + min * 60 + sec)
    dm_channel = await ctx.message.author.create_dm()
    embed_2 = discord.Embed(title=f"{ctx.message.author}님의 알람", description="시간이 되었어요!!", color = 0xCC99FF)
    await dm_channel.send(embed=embed_2)


# 홀짝
async def rand(ctx):
    dice = random.randint(1,99)
    embed = discord.Embed(title='홀, 짝 중에 하나를 선택해주세요.', description='선택 한 뒤에 어떤 수가 나왔는지 알려드려요.')
    embed.add_field(name='주사위의 눈', value='???')
    embed.add_field(name='홀수', value='🔴')
    embed.add_field(name='짝수', value='🔵')
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🔴')
    await msg.add_reaction('🔵')

    try:
        def check(reaction, user):
            return str(reaction) in ['🔴','🔵'] and user == ctx.message.author and reaction.id == msg.id
        reaction, user = await app.wait_for('reaction_add', check=check)
        if (str(reaction) == '🔴' and dice % 2 == 1) or (str(reaction) == '🔵' and dice % 2 == 0):
            embed = discord.Embed(title='홀, 짝 중에 하나를 선택해주세요.', description='정답입니다!')
        
        else:
            embed = discord.Embed(title='홀, 짝 중에 하나를 선택해주세요.', description='틀렸습니다...')

        embed.add_field(name='주사위의 눈', value=str(dice))
        embed.add_field(name='홀수', value='🔴')
        embed.add_field(name='짝수', value='🔵')
        
        await msg.clear_reactions()
        await msg.edit(embed=embed)
    except: pass

