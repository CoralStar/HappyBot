import asyncio
import json
import os
import random
from discord.utils import get
import discord #discord.py to connect to the discord API
from discord.ext import commands

client = commands.Bot(command_prefix = "w!", case_insensitive = True) #tells the bot which prefix precedes a command
TOKEN = "NzcxNzkxNjg5MjYwOTkwNDY0.X5xRBQ.e_-01Ld3RTYVDo4Gb2KrXzWy-uI"
os.chdir(r'C:\Users\Coral\OneDrive\Desktop\DiscordBot\Happy')

roleVer = 'BOT' #role to add
#user = ctx.message.author #user
role = roleVer # change the name from roleVer to role
client.remove_command('help')

@client.event
async def on_ready(): #executes anything below when the bot is ready
    print('Bot is online.')
    print(list(client.guilds))

@client.command()
async def ping(ctx):
    await ctx.send('pong!')

@client.command()
async def intro(ctx):
    await ctx.send('Hey, I am Happy! I love my owner, Alan Walker <3')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(client.guilds[1].channels, name="waiting-room")
    await channel.send('{} Welcome to The W41k3r Pr0j3ct server! Please verify that you are a Walker by taking a screenshot of your Walker Profile. An Admin will contact you or add you soon!'.format(member.mention))

@client.command()
async def hug(ctx, *, member = None):
    if member==None:
        await ctx.send('Hugs {}'.format(ctx.author.mention))
    else:
        await ctx.send('Hugs {}'.format(member))

@client.command(pass_context=True)
@commands.has_role("Admin")
async def walker(ctx, *, member = None):
    channel = discord.utils.get(client.guilds[1].channels, name="general")
    if member==None:
        await ctx.send('Please @ the user you want to be verified.')
    else:
        role = discord.utils.get(ctx.guild.roles, name="Walkers")
        await ctx.message.mentions[0].add_roles(role)
        await channel.send('{} Welcome! Feel free to introduce yourself by telling us your favorite Alan Walker song! We hope you enjoy hanging with us.'.format(member))

@client.command()
async def member_join(ctx, *, member = None):
    channel = discord.utils.get(client.guilds[1].channels, name="waiting-room")
    if member==None:
        await channel.send('Welcome to The W41k3r Pr0j3ct server! Please verify that you are a Walker by taking a screenshot of your Walker Profile. An Admin will contact you or add you soon!'.format(ctx.author.mention))
    else:
        await channel.send('{} Welcome to The W41k3r Pr0j3ct server! Please verify that you are a Walker by taking a screenshot of your Walker Profile. An Admin will contact you or add you soon!'.format(member))

@client.command()
async def verify_warning(ctx, *, member = None):
    channel = discord.utils.get(client.guilds[1].channels, name="waiting-room")
    if member==None:
        await channel.send('Welcome to The W41k3r Pr0j3ct server! Please verify that you are a Walker by taking a screenshot of your Walker Profile. If you do not respond within the next 48 hours, we will have to temporarily kick you.'.format(ctx.author.mention))
    else:
        await channel.send('{} Welcome to The W41k3r Pr0j3ct server! Please verify that you are a Walker by taking a screenshot of your Walker Profile. If you do not respond within the next 48 hours, we will have to temporarily kick you.'.format(member))

@client.command()
async def Happy(ctx, *, question):
    responses = ['As I see it, yes.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'Most likely not.',
                'Outlook not so good.',
                'Outlook good.',
                'Signs point to yes.',
                'Signs point to no.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'No.',
                'Definitely no',
                'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def roll6(ctx):
    responses = ['1',
                '2',
                '3',
                '4',
                '5',
                '6']
    await ctx.send(f'DiceRoll: {random.choice(responses)}')

@client.command()
async def coinflip(ctx):
    responses = [ 'Heads',
                'Tails']
    await ctx.send(f'CoinFlip: {random.choice(responses)}')

@client.command()
async def help(ctx):
    await ctx.send('w!intro - Introduces himself')
    await ctx.send('w!hug - Will either hug you or another member when tagged')
    await ctx.send('w!Happy - Will answer with an eightball')
    await ctx.send('w!roll6 - Will roll a 6-sided dice')
    await ctx.send('w!conflip - Heads or Tails')
    await ctx.send('w!help - Pulls up these messages again')

@client.command()
@commands.has_role("Admin")
async def adminhelp(ctx):
    await ctx.send('w!walker - Gives a member the Walkers role')
    await ctx.send('w!member_join @member - Only use this if the bot did not respond originally to the new member in the waiting-room channel')
    await ctx.send('w!verify_warning @member - If the member in the waiting-room has not responded in a given time, this message gives them a 48 hour warning prior to admin kick')

client.run(TOKEN) #runs the bot file using the unique bot token
