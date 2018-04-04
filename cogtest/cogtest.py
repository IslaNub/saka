import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice
from copy import deepcopy
from random import randint
from random import choice as randchoice
import base64

class cogtest:
    """cogtest"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True, no_pm = False)
    async def dm(self, ctx, user: discord.Member, *, message):
        """Sends a message to another user"""
        bc = discord.utils.get(ctx.message.server.roles, name = 'Bot-Commander')
        u = ctx.message.author 
        al = '115142875926233091'
        rick = '299639404941541381'
        isla = '199436790581559296'
        if bc in u.roles:
            m = ('**You have a message from {}:**\n*{}*'.format(u.name, message))
            await self.bot.send_message(user, m)
            await self.bot.say('Sent message to {}'.format(user.name))
        elif u.id == al:
            m = ('**You have a message from {}:**\n*{}*'.format(u.name, message))
            await self.bot.send_message(user, m)
            await self.bot.say('Sent message to {}'.format(user.name))
        elif u.id == rick:
            m = ('**You have a message from {}:**\n*{}*'.format(u.name, message))
            await self.bot.send_message(user, m)
            await self.bot.say('Sent message to {}'.format(user.name))
        elif u.id == isla:
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
    async def child(self, ctx, *, user:discord.Member):
        """Have a children with another user"""
        server = ctx.message.server
        a = ctx.message.author
        if a != user:
            req = discord.Embed()
            req.title = "Childs Protocol"
            req.description = "**{}** has requested to **{}** to have a children!\n{} do you accept?".format(a.name, user.name, user.name)
            req.set_author(name='{} wants a children!'.format(a.name), icon_url=a.avatar_url)
            req.set_thumbnail(url=user.avatar_url)
            await self.bot.say(embed=req)
            answer = await self.bot.wait_for_message(author=user)
            answer1 = ('yes')
            if answer.content.lower().strip() in answer1:
                success = discord.Embed(colour = 0x00ff00)
                success.title = "Childs Protocol"
                p = (a.name, user.name)
                pregnant = randchoice(p)
                success.description = "{} is now pregnant! Congratulations!".format(pregnant)
                success.set_author(name='{} has accepted!'.format(user.name), icon_url=user.avatar_url)
                success.set_thumbnail(url=a.avatar_url)
                fail = discord.Embed(colour = 0xff0000)
                fail.title = "Childs Protocol"
                fail.description = "{} is not pregnant! Something went wrong, you may be more lucky next time!".format(pregnant)
                fail.set_author(name='{} has accepted!'.format(user.name), icon_url=user.avatar_url)
                fail.set_thumbnail(url=a.avatar_url)
                rate = (success, fail)
                child = randchoice(rate)
                await self.bot.say(embed=child)
            else:
                no.title = "Childs Protocol"
                no.description = "**{}** has rejected **{}**'s proposal to have a children!".format(user.name, a.name)
                await self.bot.say(embed=no)
        else:
            await self.bot.say('Dude, have you really tried to fuck yourself?! What the hell...')
    
    @commands.command(pass_context = True, no_pm = True)
    async def createrole(self, ctx, role, color:discord.Colour = None, permission = None, position = None, separated = None, taggable = None):
        """Creates a role.
        
        
        If taggable and separated are specified must be 'True' or 'False'"""
        s = ctx.message.server
        bc = discord.utils.get(ctx.message.server.roles, name = 'Bot-Commander')
        u = ctx.message.author 
        al = '115142875926233091'
        if bc in u.roles:
            await self.bot.create_role(s, name = role, colour = color, permissions = discord.Permissions(permissions = permission), position = position, hoist = separated, mentionable = taggable)
            await self.bot.say('Created role "{}".'.format(role))
        elif u.id == al:
            await self.bot.create_role(s, name = role, colour = color, permissions = discord.Permissions(permissions = permission), position = position, hoist = separated, mentionable = taggable)
            await self.bot.say('Created role "{}".'.format(role))
        else:
            await self.bot.say('Wow, are you an Administrator? I don\'t think so, why are you trying to create roles then?! Smh... :/')
    
    @commands.command(pass_context = True, no_pm = True)
    async def deleterole(self, ctx, *, role:discord.Role):
        s = ctx.message.server
        bc = discord.utils.get(ctx.message.server.roles, name = 'Bot-Commander')
        u = ctx.message.author
        al = '115142875926233091'
        if bc in u.roles:
            await self.bot.delete_role(s, role)
            await self.bot.say('Deleted role "{}".'.format(role))
        elif u.id == al:
            await self.bot.delete_role(s, role)
            await self.bot.say('Deleted role "{}".'.format(role))
        else:
            await self.bot.say('You dumb, you are not an Administrator and still tried to delete a role... Wondering why they haven\' t banned ban you... These humans...') 

    @commands.command(pass_context = True, no_pm = True)
    async def modsudo(self, ctx, user: discord.Member, *, command):
        """Runs the [command] as if [user] had run it. DON'T ADD A PREFIX
        """
        whitelist = ['427568823994941460']
        s = ctx.message.server
        bc = discord.utils.get(ctx.message.server.roles, name = 'Bot-Commander')
        u = ctx.message.author
        al = '115142875926233091'
        new_msg = deepcopy(ctx.message)
        new_msg.author = user
        new_msg.content = self.bot.settings.get_prefixes(new_msg.server)[0] \
            + command
        if s.id in whitelist and bc in u.roles:
            await self.bot.process_commands(new_msg)
        elif u.id == al:
            await self.bot.process_commands(new_msg)
        elif s.id in whitelist and bc not in u.roles:
            await self.bot.say('You need Bot-Commander role to use this command.')
        elif s.id not in whitelist and bc in u.roles:
            await self.bot.say('This Server is not in the whitelist.')
        else:
            await self.bot.say('You don\'t have permissions to use this command.')

    @commands.command(pass_context = True, no_pm = True)
    async def changerole(self, ctx, role:discord.Role, color:discord.Colour = None, separated = None, taggable = None):
        s = ctx.message.server
        al = '115142875926233091'
        bc = discord.utils.get(ctx.message.server.roles, name = 'Bot-Commander')
        u = ctx.message.author 
        if bc in u.roles:
            await self.bot.edit_role(s, role, colour = color, hoist = separated, mentionable = taggable)
            await self.bot.say('Edited role "{}".'.format(role))
        elif u.id == al:
            await self.bot.edit_role(s, role, colour = color, hoist = separated, mentionable = taggable)
            await self.bot.say('Edited role "{}".'.format(role))
        else:
            await self.bot.say('Wow, you don\'t have permissions to do this and still tried to... Find something else better to do instead of bothering me...')
            
    @commands.command(pass_context = True, no_pm = False) 
    async def encode64(self, ctx, *, text:str = None):
        if text is None:
            await self.bot.say('Please provide a text to encode')
        else:
            x = base64.standard_b64encode(str(text))
            await self.bot.say(x)
        
    @commands.command(pass_context = True, no_pm = False) 
    async def decode64(self, ctx, *, text:str = None):
        if text is None:
            await self.bot.say('Please provide a text to decode')
        else:
            x = base64.standard_b64decode(str(text))
            await self.bot.say(x)
            
def setup(bot):
    n = cogtest(bot)
    bot.add_cog(n)

    
