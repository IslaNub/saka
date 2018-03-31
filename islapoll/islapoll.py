import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from __main__ import send_cmd_help
from random import randint
from random import choice

class islapoll:
    """Creates polls"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True, no_pm = True)
    async def createpoll(self, ctx, *, poll):
        """Creates a new poll"""
        e1 = ':white_check_mark:'
        e2 = ':negative_squared_cross_mark:'
        test = await self.bot.say('Kek')
        await self.bot.add_reaction(test, e1) 
        await self.bot.add_reaction(test, e2) 
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        u = ctx.message.author
        server = ctx.message.server
        p = discord.Embed(colour=discord.Colour(value=colour))
        avi = u.avatar_url
        p.set_thumbnail(url=server.icon_url)
        p.set_author(name= 'Poll from {}'.format(u.name), icon_url=avi)
        p.title = '{} Poll'.format(server.name)
        p.description = poll
        p.set_footer(text='IslaPoll v0.1')
        a = await self.bot.say(embed=p)
        #emojis = []
        #emotes = [':white_check_mark:', ':negative_squared_cross_mark:']
        #for em in emotes:
        #    emojis.append('{}'.format(str(em)))
        #for e in emojis:
        #    await self.bot.add_reaction(a, e)
        
        await self.bot.add_reaction(a, e1) 
        await self.bot.add_reaction(a, e2) 
        
def setup(bot):
    n = islapoll(bot)
    bot.add_cog(n)
