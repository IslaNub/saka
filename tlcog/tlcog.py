#default
import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import sys
import subprocess
import asyncio
from subprocess import Popen

#utilities
import random
from random import choice, randint
import base64
import json
import aiohttp
import itertools
import requests
from weather import Weather
import datetime
import time

#math
import math
import decimal
from decimal import Decimal, ROUND_HALF_UP, DecimalException
from math import factorial as mfac



class tlcog:
    """tlcog"""
    
    def __init__(self, bot):
        self.bot = bot
        
    
    
    #UTILITIES
    def tlm(self):
        tlservermobile = self.bot.get_server('301578535175323658')
        return tlservermobile
    
    def isla(self):
        isla = self.tlm().get_member('199436790581559296')
        return isla
      
    @commands.command(pass_context = True, no_pm = True)
    async def owner(self, ctx):
        await self.bot.say('{} is the Owner of this Bot.'.format(self.isla().name))
    
    @commands.command(pass_context=True)
    async def pingtime(self, ctx):
        """Pong."""
        t1 = time.perf_counter()
        nothing = await self.bot.get_user_info('199436790581559296')
        t2 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        
        thedata = ("**Pong.**\nTime: " + str(int(round((t2-t1)*1000)) - 100) + "ms")
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        data = discord.Embed(description=thedata, colour=discord.Colour(value=color))
        await self.bot.say(embed=data)
    
    def ae(self, a, b, c):
        ae = 'and I did this right!'
        return ae
    
    @commands.command(pass_context = True)
    async def aetest(self, ctx, a, b, c):
        await self.bot.say("Random test because AE is cool, "\
        f"{self.ae(a = a, b = b, c = f'{c}')}")
        
    @commands.command(pass_context = True, no_pm = False)
    async def winky(self, ctx):
        em = discord.Embed()
        em.set_image(url = 'https://cdn.discordapp.com/'\
                     'attachments/414094090070786058/'\
                     '481611010076180480/IMG_20180822_012935.png')
        await self.bot.say(embed = em)
        
    @commands.command(pass_context = True)
    async def giveaway(self, ctx, message_id, channel_id, emoji:discord.Emoji, winners):
        try:
            m = await self.bot.get_message(self.bot.get_channel(channel_id), message_id)
            isla = await self.bot.get_user_info('199436790581559296')
            em = discord.Embed()
            col = str('7E28CC')
            em.color = int('0x' + col, 16)
            em.title = 'Winner of 1 free month of Nitro:'
            wm = await self.bot.send_message(self.bot.get_channel(channel_id), embed = em)
            r = await self.bot.get_reaction_users(discord.Reaction(emoji = emoji, message = m))
            for x in range(0, winners):
                win1 = random.choice(r)
                em.add_field(name = 'ㅤㅤ', value = win1.mention + ' (' + win1.id + ')', inline = True)
                await self.bot.send_message(isla, win1.id)
                await self.bot.edit_message(wm, embed = em)
                r.remove(win1)
        except Exception as e:
            await self.bot.say(e)


    #MATHS
    def comb(self, x, y, rounding):
        if (x).is_integer():
            xfac = mfac(x)
        else:
            xfac = math.gamma(x + 1)
        if (y).is_integer():
            yfac = mfac(y)
        else:
            yfac = math.gamma(y + 1)
        if (x - y).is_integer():
            nfac = mfac(x - y)
        else:
            nfac = math.gamma((x - y) + 1)
        op1 = yfac * nfac
        comb = Decimal(xfac / op1)
        return Decimal(comb.quantize(Decimal('{}'.format(rounding)), rounding = ROUND_HALF_UP))
    
    @commands.command(pass_context = True, no_om = False)
    async def combinatorials(self, ctx, x, y, rounding:int = None):
        """Calculate mathematical combinatorials
        
        
        Rounding default disabled, to change the value follow this method: for x.n rounding is 1, for x.nn rounding is 10, for x.nnn rounding is 100, etc."""
        x = float(x)
        y = float(y)
        if rounding is None:
            rounding = '0'
        else:
            rounding = '.{}'.format(rounding)
        try:
            await self.bot.say(self.comb(x, y, rounding))
        except ValueError as e:
            await self.bot.say('Cannot do factorial operation for a negative number.\n```py\n{} < 0```'.format(x - y))
            await self.bot.say(e)
        except DecimalException:
            await self.bot.say('Number too big.')
          
    async def on_message(self, message):
        try:
            m = await self.bot.get_message(self.bot.get_channel('478267262080647178'), '478267290098597891')
            await self.bot.edit_message(m, int(m.content) + 1)
        except Exception as e:
            await self.bot.send_message(self.bot.get_channel('478267262080647178'), e)
            
    #STATISTICS
    def armins(self, x:int):
        armin = x
        return armin
    
    async def execute(self, command):
        p = Popen(command, cwd=os.getcwd(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while p.poll() is None:
            await asyncio.sleep(1)
        out, error = p.communicate()
        return p.returncode, out, error
    
    @commands.command(pass_context = True)
    async def exe(self, ctx, *, command):
        isla = await self.bot.get_user_info('199436790581559296')
        if ctx.message.author == isla:
            try:
                code, out, error = await self.execute([command])
            except Exception as e:
                await self.bot.say(e)
        else:
            await self.bot.say('Dangerous command, only the Owner may use it.')
                                           
    @commands.command(pass_context = True)
    async def armin(self, ctx, x:int):
        """x must be a number"""
        await self.bot.say(self.armins(x))
        await self.bot.say('What? You really thought this command would be useful?')
    
                                           
    #ANIMALS
    @commands.command(pass_context = True)
    async def doggo(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                d = await resp.json()
                m = f"{d['message']}"
                em = discord.Embed()
                em.title = 'Requested by {}'.format(ctx.message.author.name)
                em.set_image(url = m)
                await self.bot.say(embed = em)
                
    @commands.command(pass_context = True)
    async def catto(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("http://aws.random.cat/meow") as resp:
                d = await resp.json()
                m = f"{d['file']}"
                em = discord.Embed()
                em.title = 'Requested by {}'.format(ctx.message.author.name)
                em.set_image(url = m)
                await self.bot.say(embed = em)
                                           
    def animal(self, animal):
        x = random.randint(300, 500)
        y = random.randint(300, 500)
        z = "https://loremflickr.com/" + str(x) + "/" + str(y) + '/' + animal
        return z
    
    @commands.command(pass_context = True)
    async def sneakko(self, ctx):
        animal = 'snake'
        em = discord.Embed()
        em.set_image(url = self.animal(animal = animal))
        await self.bot.say(embed = em)
    
    @commands.command(pass_context = True)
    async def birddo(self, ctx):
        animal = 'bird'
        self.animal(animal = animal)
        await self.bot.say(embed = em)
        
    @commands.command(pass_context = True)
    async def panddo(self, ctx):
        animal = 'panda'
        self.animal(animal = animal)
        em = discord.Embed()
        await self.bot.say(embed = em)
                                          
    @commands.command(pass_context = True)
    async def penguin(self, ctx):
        animal = 'penguin'
        self.animal(animal = animal)
        await self.bot.say(embed = em)

def setup(bot):
    n = tlcog(bot)
    bot.add_cog(n)
