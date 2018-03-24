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
        bc = discord.utils.get(ctx.message.server.roles, name = 'Bot-Commander')
        u = ctx.message.author 
        if bc in u.roles:
            m = ('**You have a message from {}:**\n*{}*'.format(u.name, message))
            await self.bot.send_message(user, m)
            await self.bot.say('Sent message to {}'.format(user.name))
        else:
            await self.bot.say('You don\'t have permissions to use this command.')
            
    @commands.command(pass_context = True, no_pm = True)
    async def pfp(self, ctx, *, user: discord.Member = None):
        """Sends the user profile picture, if user is none then sends yours"""
        if user is None:
            user = ctx.message.author
            pass
        m = ('Profile Picture for **{}**:\n{}'.format(user.name, user.avatar_url))
        await self.bot.say(m)
        
    @commands.command(pass_context = True, no_pm = True)
    async def game(self, ctx, *, user:discord.Member = None):
        if user is None:
            user = ctx.message.author
            pass
        if user.game is None:
            g = '**{}** is chilling.'.format(user.name)
        elif user.game.url is None:
            g = '**{}** is playing {}.'.format(user.name, user.game)
        else:
            g = '**{}** is streaming: [{}]({}).'.format(user.name, user.game, user.game.url)
        if user.id == '383190461512155136':
            g = '**{}** is a fucking idiot.'.format(user.name)
        await self.bot.say(g)
            
def setup(bot):
    n = cogtest(bot)
    bot.add_cog(n)
