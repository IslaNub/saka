import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice
from random import randint
from random import choice as randchoice

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
        """Sends in chat what that user is playing, if user is none then sends yours""" 
        if user is None:
            user = ctx.message.author
            pass
        if user.game is None:
            g = '**{}** is chilling.'.format(user.name)
        elif user.game.url is None:
            g = '**{}** is playing {}.'.format(user.name, user.game)
        else:
            g = '**{}** is streaming: [{}]({}).'.format(user.name, user.game, user.game.url)
        await self.bot.say(g)
            
    @commands.command(pass_context = True, no_pm = True)
    async def embedme(self, ctx, *, msg):
        """Sends your message as embed"""
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        u = ctx.message.author
        server = ctx.message.server
        em = discord.Embed(colour=discord.Colour(value=colour))
        avi = u.avatar_url
        em.set_thumbnail(url=server.icon_url)
        em.set_author(name= 'Embed from {}'.format(u.name), icon_url=avi)
        em.title = '{} Embeds'.format(server.name)
        em.description = msg
        em.set_footer(text='Thanks for choosing {}!'.format(server.name))
        await self.bot.say(embed=em)
        await self.bot.delete_message(ctx.message)
        
    @commands.command(pass_context = True, no_pm = False)
    async def nudes(self, ctx):
        """Sends nudes"""
        await self.bot.say('nudes')
        
    @commands.command(pass_context = True, no_pm = True) 
    async def child(self, ctx, user:discord.Member):
        """Have a children with another user"""
        server = ctx.message.server
        a = ctx.message.author
        req = discord.Embed()
        req.title = "Childs Protocol"
        req.description = "**{}** has requested to **{}** to have a children!\n{} do you accept?".format(a.name, user.name, user.name)
        req.set_author(name='{} wants a children!'.format(a.name), icon_url=a.avatar_url)
        req.set_thumbnail(url=user.avatar_url)
        await self.bot.say(embed=req)
        answer = await self.bot.wait_for_message(author=user)
        answer1 = ('yes')
        if answer.content.lower().strip() in answer1:
            await self.bot.say('Test')
        else:
            no = discord.Embed()
            no.title = "Childs Protocol"
            no.description = "**{}** has rejected **{}**'s proposal to have a children!".format(user.name, a.name)
            await self.bot.say(embed=no)
    
        
def setup(bot):
    n = cogtest(bot)
    bot.add_cog(n)
