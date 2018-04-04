import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from __main__ import send_cmd_help
from random import randint
from random import choice
from random import choice as randchoice

class islapoll:
    """Creates polls"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True, no_pm = True)
    async def createpoll(self, ctx, *, poll):
        """Creates a new poll"""
        e1 = '✅'
        e2 = '❎'
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
        await self.bot.delete_message(ctx.message)
        
    @commands.command(pass_context = True, no_pm = True)
    async def gn(self, ctx):
        a = ctx.message.author
        IN = '199436790581559296'
        if a.id = IN:
            n = discord.Embed(colour = 0x8A0707)
        else:
            n = discord.Embed(colour = 0x191970)
        avi = a.avatar_url
        if a.id = IN:
            images = ('https://goo.gl/images/6GLn4X', 'https://goo.gl/images/3Nfo1P')
        else:
            images = ('https://cdn.shopify.com/s/files/1/1698/6547/files/starcatalog_600x600.jpg?v=1511346010', 'https://wallpapertag.com/wallpaper/middle/7/1/c/544439-best-nighttime-wallpaper-2560x1440-for-phone.jpg', 'https://i.pinimg.com/originals/bc/6e/fc/bc6efc08653224473f590eab54647da4.jpg', 'http://www.newhdwallpaper.in/wp-content/uploads/2014/07/Good-night-time-best-wishes.jpg', 'https://ak5.picdn.net/shutterstock/videos/5633555/thumb/3.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEsvQm_6YaslxY9lOIu5kMXxL174x4PXTwYetByCx70Xqot9uQ')
        image = randchoice(images)
        n.set_thumbnail(url = image)
        if a.id == IN:
            n.set_author(name= '{} is going to die!'.format(a.name), icon_url=avi)
        else:
            n.set_author(name= '{} is going to sleep!'.format(a.name), icon_url=avi)
        if a.id == IN:
            n.description = '{} is dying and says good-bye to all his little boys and girls.'.format(a.name)
        else:
            n.description = '{} says good night to all his little boys and girls.'.format(a.name)
        if a.id == IN:
            n.set_footer(text = 'Enjoy your life!')
        else:
            n.set_footer(text = 'Good Night!')
        await self.bot.say(embed = n)

def setup(bot):
    n = islapoll(bot)
    bot.add_cog(n)
