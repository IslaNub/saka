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
import json
import aiohttp
import itertools

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
    async def pfp(self, ctx, user: discord.Member = None, hd = None):
        """Sends the user profile picture, if user is none then sends yours
        
        
        HD default set to yes"""
        if user is None:
            user = ctx.message.author
            pass
        if hd is None:
            strip = ''
            pass
        if hd is not None and hd.lower().strip() == 'yes':
            strip = ''
            pass
        if hd is not None and hd.lower().strip() == 'no':
            strip = '?size=1024'
        pfp = discord.Embed()
        pfp.title = ('Profile Picture for {}:'.format(user.name))
        pfp.set_image(url = '{}'.format(user.avatar_url.strip(strip)))
        await self.bot.say(embed = pfp)
        
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
                no = discord.Embed(colour = 0xff0000)
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
        isla = '199436790581559296' 
        if bc in u.roles:
            await self.bot.create_role(s, name = role, colour = color, permissions = discord.Permissions(permissions = permission), position = position, hoist = separated, mentionable = taggable)
            await self.bot.say('Created role "{}".'.format(role))
        elif u.id == isla:
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
        whitelist = ['427568823994941460', '390056984650579978']
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
  
    @commands.command(pass_context = True, no_pm = True)
    async def print(self, ctx, *, message):
        """Uses Python to print your message"""
        msg = message
        await self.bot.say('```{}```'.format(msg))
        
    @commands.command(pass_context = True, no_pm = True) 
    async def crime(self, ctx, *, user:discord.Member):
        """Soon..."""

    @commands.command(pass_context = True, no_pm = True)
    async def msgreplace(self, ctx, id, to_be_replaced, to_replace):
        """Uses Python to replace words/letters from an already existing message
        
        
        Must be run in the message channel"""
        tbr = to_be_replaced
        tr = to_replace
        msg = await self.bot.get_message(ctx.message.channel, id)
        await self.bot.say(msg.content.replace(tbr, tr))
        
    @commands.command(pass_context = True, no_pm = True)
    async def yomom(self, ctx, user:discord.Member = None):
        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.yomomma.info") as resp:
                d = await resp.json()
                m = f"{d['joke']}"
                if user is not None:
                    m = f"{user.mention} {d['joke']}"
                    isla = await self.bot.get_user_info('199436790581559296')
                    if user.id == isla.id:
                        user = ctx.message.author
                        m = f"{user.mention} you think you're clever?! Well, so...\n{d['joke']}"
                        pass
                    pass
                await self.bot.say(m)
        
    @commands.command(pass_context = True, no_pm = True)
    @commands.has_permissions(manage_emojis = True)
    async def newemote(self, ctx, name: str, id: int):
        """Adds an emote to the Server from an already existing emote (ID required)"""
        try:
            async with aiohttp.ClientSession() as session:
                e = f"https://cdn.discordapp.com/emojis/{id}"
                async with session.get(e) as resp:
                    b = await resp.read()
                    await self.bot.create_custom_emoji(ctx.message.server, name = name, image = b)
                    msg = discord.Embed()
                    msg.title = 'Created new emote:'
                    msg.set_image(url = '{}'.format(e))
                    await self.bot.say(embed = msg)
        except Exception as e:
            await self.bot.say('Something went wrong, make sure ID exists.')
            print(e)

    @commands.command(pass_context = True, no_pm = True)
    @commands.has_permissions(manage_emojis = True)
    async def deleteemote(self, ctx, emote:discord.Emoji):
        """Deletes an emote from the Server"""
        try:
            await self.bot.delete_custom_emoji(emote)
            await self.bot.say('Successfully deleted the emote!')
        except Exception as e:
            await self.bot.say('Something went wrong, the emote wasn\'t deleted.')
            print(e)
        
    @commands.command(pass_context = True, no_pm = True)
    @commands.has_permissions(manage_emojis = True)
    async def createemote(self, ctx, name: str, link: str):
        """Adds an emote to the Server using URL"""
        try:
            async with aiohttp.ClientSession() as session:
                e = link
                async with session.get(e) as resp:
                    b = await resp.read()
                    await self.bot.create_custom_emoji(ctx.message.server, name = name, image = b)
                    msg = discord.Embed()
                    msg.title = 'Created new emote:'
                    msg.set_image(url = '{}'.format(e))
                    await self.bot.say(embed = msg)
        except Exception as e:
            await self.bot.say(e)
            print(e)

    @commands.command(pass_context = True, no_pm = True) 
    async def getmessage(self, ctx, message_ID, channel_ID = None):
        mID = message_ID
        cID = channel_ID
        c = self.bot.get_channel(cID)
        if channel_ID is None:
            c = ctx.message.channel
            pass
        m = await self.bot.get_message(c, mID)
        await self.bot.say(m.content)
            
    @commands.command(pass_context = True, no_pm = False)
    async def trolling(self, ctx, id:discord.Member, *, message):
        
        try:
            
            if ctx.message.author.id == '199436790581559296':
                await self.bot.send_message(id, message)
                await self.bot.say('Done.')
            else:
                pass
        except Exception as e:
            await self.bot.say(e)
        
    @commands.command(pass_context = True, no_pm = True)
    async def membersperrole(self, ctx, role:discord.Role):
        server = ctx.message.server 
        u = ctx.message.author
        a = discord.utils.get(server.roles, name = 'Admin')
        if a in u.roles:
            try:
                x = 0
                m = await self.bot.say('List of the members with **{}** role:'.format(role.name))
                count = await self.bot.say('**{}** members have this role.'.format(x))
                for member in ctx.message.server.members:
                    if role in member.roles:
                        if len(m.content) > 1800:
                            m = await self.bot.say(f'{member.name}')
                            x += 1
                            count = await self.bot.edit_message(count, '**{}** members have this role.'.format(x))
                        else:
                            m = await self.bot.edit_message(m, f'{m.content}\n{member.name}')
                            x += 1
                            if x >= 2 or x < 1:
                                cp = 's'
                                gc = 've'
                                pass
                            if x == 1:
                                cp = ''
                                gc = 's'
                                pass
                            count = await self.bot.edit_message(count, '**{}** member{} ha{} this role.'.format(x, cp, gc))
            except Exception as e:
                await self.bot.say(e)

    @commands.command(pass_context = True, no_pm = True)
    async def getbans(self, ctx):
        try:
            ser = ctx.message.server
            b = await self.bot.get_bans(ser)
            x = 0
            bc = discord.utils.get(ser.roles, name = 'Admin')
            u = ctx.message.author
            if bc in u.roles:
                m = await self.bot.say(b[x].name)
                while True:
                    try:
                        x += 1
                        m = await self.bot.edit_message(m, f'{m.content}\n{b[x].name}')
                    except Exception:
                        break
                await self.bot.say('**{} users are banned from this Server.**'.format(len(b)))
            else:
                await self.bot.say('You are not allowed to use this command, only {} can.'.format(bc.name))
        except Exception as e:
            await self.bot.say(e)
            print(e)
        
    @commands.command(pass_context = True, no_pm = True) 
    async def testemembersperrole(self, ctx, role:discord.Role):
        server = ctx.message.server 
        u = ctx.message.author
        a = discord.utils.get(server.roles, name = 'Admin')
        if a in u.roles:
            try:
                m = await self.bot.say('List of the members with **{}** role:'.format(role.name))
                async for member in ctx.message.server.members:
                    if role in member.role:
                        while True:
                            try:
                                m = await self.bot.edit_message(m, f'{m.content}\n{member.name}')
                            except Exception as e:
                                break
                                await self.bot.say(e)
            except Exception as e:
                await self.bot.say(e)

    @commands.command(pass_context = True, no_pm = True)
    async def ultraembed(self, ctx, user:discord.Member = None):
        try:
            zrib = await self.bot.get_user_info('196924268360105984')
            z = discord.Embed()
            """z.set_author(name = 'Zrib should be using this...', icon_url = zrib.avatar_url)
            z.description = 'Please use [this](https://discord.gg/royalerecruit) Server for recruiting or searching for a clan.'
            z.title = 'Recruit Server'
            z.set_footer(text = 'Have a nice day!', icon_url = ctx.message.server.icon_url)
            if user is not None:
                z.set_thumbnail(url = user.avatar_url)
                pass"""
            if user is None:
                user = ctx.message.author
                pass
            z.set_author(name = 'ㅤㅤ', icon_url = user.avatar_url)
            z.set_thumbnail(url = user.avatar_url)
            z.set_image(url = user.avatar_url)
            z.set_footer(text = 'ㅤㅤ', icon_url = user.avatar_url)
            await self.bot.say(embed = z)
        except TypeError as e:
            await self.bot.say(e) 
            
    @commands.has_permissions(ban_members = True)
    @commands.command(pass_context = True, no_pm = True)
    async def announcement(self, ctx, text, image_url, color:discord.Colour):
        image = image_url
        embed = discord.Embed(colour = color)
        embed.description = text
        embed.set_image(url = image)
        await self.bot.say(embed = embed)
            
    @commands.has_permissions(kick_members = True)
    @commands.command(pass_context = True, no_pm = True)
    async def createinvite(self, ctx):
        welcome = self.bot.get_channel('439537529553944591')
        invite = await self.bot.create_invite(welcome)
        await self.bot.say(invite)
        
    @commands.has_permissions(kick_members = True)
    @commands.command(pass_context = True, no_pm = True)
    async def getinvites(self, ctx):
        invites = await self.bot.invites_from(ctx.message.server)
        x = 0
        ninvites = len(invites)
        if ninvites == 0 or ninvites >= 2:
            p = 's'
            pass
        if ninvites == 1:
            p = ''
            pass
        await self.bot.say('{} invite{} created for this Server, want to get a list?'.format(ninvites, p))
        try:
            a = await self.bot.wait_for_message(author = ctx.message.author, timeout = 15)
            pass
        except Exception:
            await self.bot.say('Okay, canceling operation.')
            return
        if a.content.lower().strip() == 'yes':    
            m = await self.bot.say(invites[x])
            while True:
                try:
                    x += 1
                    m = await self.bot.edit_message(m, f'{m.content}\n{invites[x]}')
                except Exception:
                    break
        else:
            await self.bot.say('Okay, canceling operation.')
    
    @commands.has_permissions(kick_members = True)
    @commands.command(pass_context = True, no_pm = True)
    async def inviteinfo(self, ctx, invite_link):
        i = await self.bot.get_invite(invite_link)
        e = discord.Embed(color = 0x7289DA)
        e.title = 'Information for invite "{}"'.format(invite_link)
        e.url = invite_link
        e.add_field(name = 'Created by:', value = i.inviter, inline = True)
        await self.bot.say(embed = e)
    
    @commands.command(pass_context = True, no_pm = True)
    async def getcolor(self, ctx, hex:str):
        em = discord.Embed()
        hex = hex.strip('#')
        url = "https://api.color.pizza/v1/{}".format(hex)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
        hexapi = 'http://www.htmlcsscolor.com/preview/gallery/{}.png'.format(data["colors"][0]["hex"].strip('#'))
        em.set_image(url = hexapi)
        em.color = int('0x' + hex, 16)
        em.add_field(name = 'Name:', value = data["colors"][0]["name"], inline = True)
        em.add_field(name = 'Hex:', value = data["colors"][0]["hex"].upper(), inline = True)
        em.add_field(name = 'RGB:', value = 'R: ' + str(data["colors"][0]["rgb"]["r"]) + '; G: ' + str(data["colors"][0]["rgb"]["g"]) + '; B: ' + str(data["colors"][0]["rgb"]["b"]), inline = True)
        em.add_field(name = 'Luminance:', value = data["colors"][0]["luminance"], inline = True)
        em.add_field(name = 'Distance:', value = data["colors"][0]["distance"], inline = True)
        em.add_field(name = 'Requested Hex:', value = data["colors"][0]["requestedHex"].upper(), inline = True)
        em.set_footer(text = '<== Original requested color; other color\'s values might be approximated', icon_url = "http://www.htmlcsscolor.com/preview/gallery/{}.png".format(data["colors"][0]["requestedHex"].strip('#')))
        await self.bot.say(embed = em)
    
    async def on_message(self, message):
        m = 'Who is the cutest trap in the world?'
        if message.server.id == '301578535175323658':
            emote1 = '<:PandaLove:422749996278874113>'
            emote2 = '<:AstolfoWink:422750689551319040>'
            pass
        if message.server.id == '390056984650579978':
            emote1 = '<:PandaLove:425665250285584384>'
            emote2 = '<:AstolfoWink:428192257380974602>'
            pass
        isla = await self.bot.get_user_info('199436790581559296')
        if message.author == isla and message.content == m:
            msg = 'You are, my master! {}'.format(emote1)
            await self.bot.send_message(message.channel, msg)
            return
        if message.content == m:
            msg = '{} is the cutest trap in the world! {}'.format(isla.mention, emote2)
            await self.bot.send_message(message.channel, msg)
 
    @commands.command(pass_context = True, no_pm = True)
    async def getemote(self, ctx, emote:discord.Emoji):
        em = discord.Embed()
        em.set_image(url = emote.url)
        await self.bot.say(embed = em)
        
    @commands.group(name = "bracket", pass_context = True)
    async def _bracket(self, ctx):
        """Add/remove bracket role"""
        u = ctx.message.author
        mod = discord.utils.get(ctx.message.server.roles, name = 'Community Moderator')
        if u.id == '330643078023217155' and ctx.invoked_subcommand is None or mod in u.roles and ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            
    @_bracket.command(pass_context = True, no_pm =  True)
    async def add(self, ctx, user:discord.Member):
        """Add the bracket role"""
        u = ctx.message.author
        bracket = discord.utils.get(ctx.message.server.roles, name = 'Bracket')
        mod = discord.utils.get(ctx.message.server.roles, name = 'Community Moderator')
        if u.id == '330643078023217155' and ctx.invoked_subcommand is None or mod in u.roles and ctx.invoked_subcommand is None:
            if bracket in user.roles:
                await self.bot.say('This user already have this role')
                return
            if bracket not in user.roles:
                await self.bot.add_roles(user, bracket)
                await self.bot.say('Added {} to {}.'.format(bracket.name, user.name))
        else:
            await self.bot.say('You can\'t use this command.')
            
    @_bracket.command(pass_context = True, no_pm =  True)
    async def remove(self, ctx, user:discord.Member):
        """Remove the bracket role"""
        u = ctx.message.author
        bracket = discord.utils.get(ctx.message.server.roles, name = 'Bracket')
        mod = discord.utils.get(ctx.message.server.roles, name = 'Community Moderator')
        if u.id == '330643078023217155' and ctx.invoked_subcommand is None or mod in u.roles and ctx.invoked_subcommand is None:
            if bracket not in user.roles:
                await self.bot.say('This user doesn\'t have this role.')
            if bracket in user.roles:
                await self.bot.remove_roles(user, bracket)
                await self.bot.say('Removed {} from {}.'.format(bracket.name, user.name))
                return
        else:
            await self.bot.say('You can\'t use this command.')

    async def on_message(self, message):
        isla = await self.bot.get_user_info('199436790581559296')
        armin = await self.bot.get_user_info('200467543968710656')
        e = '[embed this]'
        if message.content.startswith('+') or message.attachments or '@' in message.content:
            return
        if e in message.content.lower() and message.content.lower().strip() != e \
        or message.author.id in [isla.id, armin.id] and message.channel.id == '449897068845203470': # Remember the continuation line
            em = discord.Embed()
            em.color = discord.Color(value = 0x00FFBF)
            em.title = message.author.name
            em.description = message.content.replace(e, '').replace(e.capitalize(), '')
            em.set_thumbnail(url = message.author.avatar_url)
            await self.bot.send_message(message.channel, embed = em)
            await self.bot.delete_message(message)
            return
        else:
            return
            
def setup(bot):
    n = cogtest(bot)
    bot.add_cog(n)

    
    
