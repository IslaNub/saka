import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help

class cogtest:
    """cogtest"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True, no_pm = True)
    async def dm(self, ctx, user: discord.Member = None, message):
        """Sends a message to another user"""
        await self.bot.say('{} {}'.format(user, message))
        m = ('You have a message from {}:\n{}'.format(ctx.message.author.name, message))
        await self.bot.say('{} {}'.format(user, m))
        await self.bot.send_message(user, m)
        await self.bot.say('Sent message to {}'.format(user.name))

def setup(bot):
    n = cogtest(bot)
    bot.add_cog(n)
