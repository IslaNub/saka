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
        Alex = '327429593067683840'
        if a.id == IN:
            n = discord.Embed(colour = 0x8A0707)
        else:
            n = discord.Embed(colour = 0x191970)
        avi = a.avatar_url
        if a.id == IN:
            images = ('https://i.pinimg.com/originals/67/e1/73/67e173bbadbd41caccf4654760684b19.jpg', 'https://i.pinimg.com/originals/19/9e/e4/199ee4174eab3bfa3142c102e196a2f3.jpg', 'http://2.bp.blogspot.com/-rtUeJkZQp2A/VTeBJYuygDI/AAAAAAAAAnM/RtGsuI1VJ1k/w1200-h630-p-k-no-nu/blood-death-emo-knife-sad-Favim.com-115129.jpg', 'http://2.bp.blogspot.com/-9k9EEkQ1ALQ/T2zFtKavEpI/AAAAAAAACLM/xMJul8_6oTc/s1600/love_hurts_a_lot-764464.jpg')
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
        elif a.id == Alex:
            n.description = '{} says good night to all his cute boys and girls.'.format(a.name)
        else:
            n.description = '{} says good night to all his cute little boys and girls.'.format(a.name)
        if a.id == IN:
            n.set_footer(text = 'Enjoy your life!')
        else:
            n.set_footer(text = 'Good Night!')
        await self.bot.say(embed = n)
        
    @commands.command(pass_context = True, no_pm = True)
    async def gm(self, ctx):
        a = ctx.message.author
        IN = '199436790581559296'
        Alex = '327429593067683840'
        if a.id == IN:
            n = discord.Embed(colour = 0x5E0000)
        else:
            n = discord.Embed(colour = 0x00BFFF)
        avi = a.avatar_url
        if a.id == IN:
            images = ('https://i.pinimg.com/originals/59/91/be/5991be64ff7a5bc35cf78b3de1c81ccd.jpg', 'https://i.ytimg.com/vi/epgi78q5OdM/maxresdefault.jpg', 'https://i.ytimg.com/vi/MGHtwbp-wfY/maxresdefault.jpg', 'https://i.pinimg.com/originals/be/b2/22/beb22246dbb74ee3643eb80fe97d111a.jpg', 'http://churchandstate.org.uk/wordpressRM/wp-content/uploads/2015/12/hell.jpg')
        else:
            images = ('https://i.ytimg.com/vi/8Hedq2d1H44/maxresdefault.jpg', 'https://cdn.pixabay.com/photo/2016/08/31/17/41/sunrise-1634197_1280.jpg', 'https://techcrunch.com/wp-content/uploads/2015/10/shutterstock_112249904.jpg', 'https://images.unsplash.com/photo-1504270159110-876cfaca9ece?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=874a6efa6345d66b76fde4099fa67757&w=1000&q=80')
        image = randchoice(images)
        n.set_thumbnail(url = image)
        if a.id == IN:
            n.set_author(name= '{} is dead!'.format(a.name), icon_url=avi)
        else:
            n.set_author(name= '{} has just woken up!'.format(a.name), icon_url=avi)
        if a.id == IN:
            n.description = '{} is peacefully resting in the Darkness...'.format(a.name)
        elif a.id == Alex:
            n.description = '{} says good morning to all his cute boys and girls.'.format(a.name)
        else:
            n.description = '{} says good morning to all his cute little boys and girls.'.format(a.name)
        if a.id == IN:
            n.set_footer(text = 'Warm regards from the Hell!')
        else:
            n.set_footer(text = 'Good Morning!')
        await self.bot.say(embed = n)

    #@commands.group(pass_context = True, no_pm = True, invoke_without_command = True)
    #async def editchannelperms(self, ctx, role : discord.Role, channel : discord.Channel, read_messages, send_messages):
    #    mng = discord.utils.get(ctx.message.server.roles, name = 'Managers')
    #    author = ctx.message.author
    #    server = ctx.message.server
    #    if mng in author.roles:
    #        if ctx.invoked_subcommand is None:
    #            await ctx.invoke(self.channel_editchannelperms, role = role)
    #    else:
    #        await self.bot.say('You can\'t use this command.')
        
    @commands.command(pass_context = True, no_pm = True)
    async def editchannelperms(self, ctx, role : discord.Role, channel : discord.Channel = None, read_messages, send_messages):
        """Edit permissions"""
        author = ctx.message.author
        server = ctx.message.server
        rm = read_messages
        sm = send_messages
        overwrite = discord.PermissionOverwrite()
        if rm == 'True':
            overwrite.read_messages = True
        elif rm == 'False':
            overwrite.read_messages = False
        else:
            pass
        if sm == 'True':
            overwrite.send_messages = True
        elif sm == 'False':
            overwrite.send_messages = False
        else:
            pass
        mng = discord.utils.get(server.roles, name = 'Managers')
        if mng in author.roles:
            if channel is None and channel == 'server':
                for channel in server.channels:
                    await self.bot.edit_channel_permissions(channel, role, overwrite)
            else:
                await self.bot.edit_channel_permissions(channel, role, overwrite)
            if rm != 'True' and rm != 'False':
                rm = 'null'
                pass
            if sm != 'True' and sm != 'False':
                sm = 'null'
                pass
            await self.bot.say('Edited permissions for {} in {}:\n```Read messages= {}\nSend messages= {}```'.format(role.mention, channel.mention, rm, sm))
        else:
            await self.bot.say('You can\'t use this command.')

def setup(bot):
    n = islapoll(bot)
    bot.add_cog(n)
