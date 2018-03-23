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
    async def dm(self, ctx, user: discord.Member, *, message):
        """Sends a message to another user"""
        m = ('**You have a message from {}:**\n*{}*'.format(ctx.message.author.name, message))
        await self.bot.send_message(user, m)
        await self.bot.say('Sent message to {}'.format(user.name))
        
    @commands.command(pass_context = True, no_pm = True)
    async def pfp(self, ctx, user: discord.Member = None):
        """Sends the user profile picture, if user is none then sends yours"""
        if user is None:
            user = ctx.message.author
            pass
        m = ('Profile Picture for **{}**:\n{}'.format(user.name, user.avatar_url))
        await self.bot.say(m)
            
def setup(bot):
    n = cogtest(bot)
    bot.add_cog(n)
