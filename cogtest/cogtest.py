import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help

class cogtest:
    """cogtest"""
    
    def __init__(self, bot):
        self.bot = bot
    
    async def bhavya(self, message):
        """Sends a message to Bhavya"""
        b = self.bot.get_user('383190461512155136')
        await self.bot.send_message(b, message)
        await self.bot.say('Sent message to {}'.format(u.mention))

def setup(bot):
    n = cogtest(bot)
    bot.add_cog(n)
