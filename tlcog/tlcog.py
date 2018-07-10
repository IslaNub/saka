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
from decimal import Decimal
from math import factorial as mfac


class tlcog:
    """tlcog"""
    
    def __init__(self, bot):
        self.bot = bot
        
    def tlm(self):
        tlservermobile = self.bot.get_server('301578535175323658')
        return tlservermobile
    
    def isla(self):
        isla = self.tl().get_member('199436790581559296')
        return isla
      
    @commands.command(pass_context = True, no_pm = True)
    async def owner(self, ctx):
        await self.bot.say('{} is the Owner of this Bot.'.format(self.isla().name)        

                           
def setup(bot):
    n = tlcog(bot)
    bot.add_cog(n)
