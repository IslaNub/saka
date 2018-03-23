import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help

class cogtest:
    """cogtest"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True, is_private = True)
    async def bhavya(self, ctx, message):
        """Sends a message to Bhavya"""
        u = '<@199436790581559296>'
        await self.bot.say('Kek1')

        await self.bot.say('{} {}'.format(u, u))
        await self.bot.send_message('IslaNub#8347', message)
        await self.bot.say('Sent message to {}'.format(u))

def setup(bot):
    n = cogtest(bot)
    bot.add_cog(n)
