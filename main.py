from asyncio import events
import discord
import os
import asyncio
import math
from random import randint
from discord.utils import get
import time

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('League of Shawty love'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!challenge'):
        if len(message.mentions) != 1:
            return await message.channel.send('Mention a player!')

        opponent = message.mentions[0]
        emoji = '<:swordexclamation:968268304001151026>'
        msg = await message.channel.send(f'**{message.author.name}** is challenging **{opponent.name}**! React to accept')
        await msg.add_reaction(emoji)

        def check(react, usr):
            return (str(react.emoji) == emoji 
            and usr == opponent
            and react.message == msg)

        try:
            reaction, user = await client.wait_for('reaction_add', check=check, timeout=10)
        except asyncio.TimeoutError:
            return await message.channel.send("Opponent didn't accept")
        
        embed=discord.Embed(title="Round # 0", description=f'{message.author.name} v/s {opponent.name}', color=0x8cff00)
        embed.add_field(name="Starting match...", value="Get prepared!", inline=False)
        round_status = await message.channel.send(embed=embed)
        time.sleep(3)
        
        embed=discord.Embed(title='Round # 1', description=f'{message.author.name} v/s {opponent.name}', color=0xff6600)
        embed.add_field(name=f"{message.author.name} absolutely destroys {opponent.name} and takes the win!", value=f"Fuck you {opponent.name}", inline=False)
        await round_status.edit(embed=embed)
        

        
        

client.run();  