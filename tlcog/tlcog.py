#default
import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help

#utilities
import random
from random import choice
from random import randint
import base64
import json
import aiohttp
import itertools

#math
import math
import decimal
from decimal import Decimal, ROUND_HALF_UP
from math import factorial as mfac


class tlcog:
    """tlcog"""
    
    def __init__(self, bot):
        self.bot = bot
        
    def tlm(self):
        tlservermobile = self.bot.get_server('301578535175323658')
        return tlservermobile
    
    def isla(self):
        isla = self.tlm().get_member('199436790581559296')
        return isla
    
    def comb(self, x:int, y:int):
        xfac = mfac(x)
        yfac = mfac(y)
        nfac = mfac(x - y)
        op1 = yfac * nfac
        comb = Decimal(xfac / op1)
        return Decimal(comb.quantize(Decimal('0'), rounding = ROUND_HALF_UP))
      
    @commands.command(pass_context = True, no_pm = True)
    async def owner(self, ctx):
        await self.bot.say('{} is the Owner of this Bot.'.format(self.isla().name))
    
    @commands.command(pass_context = True, no_om = False)
    async def combinatorials(self, ctx, x:int, y:int):
        await self.bot.say(self.comb(x, y))
    
                           
def setup(bot):
    n = tlcog(bot)
    bot.add_cog(n)
