#default
import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help

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

    async def on_message(self, message):
        m = await self.bot.get_message(self.bot.get_channel('432918480371712000'), '469478988608307200')
        if 'xd' in message.content.lower() and message.author.id == '330643078023217155':
            m = await self.bot.edit_message(m, int(m.content) + 1)
    
    @commands.command(pass_context = True, no_pm = True)
    async def jorisxd(self, ctx):
        m = await self.bot.get_message(self.bot.get_channel('432918480371712000'), '469478988608307200')
        await self.bot.say('Joris has said XD {} times!'.format(m.content))
        
        
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
          
        
            
    #STATISTICS
    def armins(self, x:int):
        armin = x
        return armin
    
    @commands.command(pass_context = True)
    async def armin(self, ctx, x:int):
        """x must be a number"""
        await self.bot.say(self.armins(x))
        await self.bot.say('What? You really thought this command would be useful?')
                    
def setup(bot):
    n = tlcog(bot)
    bot.add_cog(n)
