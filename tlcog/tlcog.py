#default
import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import sys
import subprocess
import asyncio
from subprocess import Popen
import traceback

#utilities
from .utils.chat_formatting import escape_mass_mentions, italics, pagify
import random
from random import choice, randint
import base64
import json
import aiohttp
import itertools
import requests
import re
from weather import Weather
import datetime
import time
from copy import deepcopy

#math
import math
import decimal
from decimal import Decimal, ROUND_HALF_UP, DecimalException
from math import factorial as mfac

#LISTS
animals_list = ['dolphin', 'tiger', 'bunny', 'rabbit', 'lion', 'cat', 'dog', 'fish', 'snake', 'panda', 'turtle', 'bird', 'bear', 'koala', 'penguin', 'red panda']

class tlcog:
    """tlcog"""
    
    def __init__(self, bot):
        self.bot = bot
        
    
    
    #UTILITIES
    def tlm(self):
        tlservermobile = self.bot.get_server('301578535175323658')
        return tlservermobile
    
    def isla(self):
        isla = self.tlm().get_member('199436790581559296')
        return isla
      
    @commands.command(pass_context = True, no_pm = True)
    async def owner(self, ctx):
        await self.bot.say('{} is the Owner of this Bot.'.format(self.isla().name))
    
    @commands.command(pass_context=True)
    async def pingtime(self, ctx):
        """Pong."""
        t1 = time.perf_counter()
        nothing = await self.bot.get_user_info('199436790581559296')
        t2 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        
        thedata = ("**Pong.**\nTime: " + str(int(round((t2-t1)*1000)) - 100) + "ms")
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        data = discord.Embed(description=thedata, colour=discord.Colour(value=color))
        await self.bot.say(embed=data)
    
    def ae(self, a, b, c):
        ae = 'and I did this right!'
        return ae
    
    @commands.command(pass_context = True)
    async def aetest(self, ctx, a, b, c):
        await self.bot.say("Random test because AE is cool, "\
        f"{self.ae(a = a, b = b, c = f'{c}')}")
        
    @commands.command(pass_context = True, no_pm = False)
    async def winky(self, ctx):
        em = discord.Embed()
        em.set_image(url = 'https://cdn.discordapp.com/'\
                     'attachments/414094090070786058/'\
                     '481611010076180480/IMG_20180822_012935.png')
        await self.bot.say(embed = em)
        
    @commands.command(pass_context = True)
    async def giveaway(self, ctx, message_id, channel_id, emoji:discord.Emoji, winners):
        try:
            m = await self.bot.get_message(self.bot.get_channel(channel_id), message_id)
            isla = await self.bot.get_user_info('199436790581559296')
            em = discord.Embed()
            col = str('7E28CC')
            em.color = int('0x' + col, 16)
            em.title = 'Winner of 1 free month of Nitro:'
            wm = await self.bot.send_message(self.bot.get_channel(channel_id), embed = em)
            r = await self.bot.get_reaction_users(discord.Reaction(emoji = emoji, message = m))
            for x in range(0, winners):
                win1 = random.choice(r)
                em.add_field(name = 'ㅤㅤ', value = win1.mention + ' (' + win1.id + ')', inline = True)
                await self.bot.send_message(isla, win1.id)
                await self.bot.edit_message(wm, embed = em)
                r.remove(win1)
        except Exception as e:
            await self.bot.say(e)


    #MATHS
    def comb(self, x, y, rounding):
        if (x).is_integer():
            xfac = mfac(x)
        else:
            xfac = math.gamma(x + 1)
        if (y).is_integer():
            yfac = mfac(y)
        else:
            yfac = math.gamma(y + 1)
        if (x - y).is_integer():
            nfac = mfac(x - y)
        else:
            nfac = math.gamma((x - y) + 1)
        op1 = yfac * nfac
        comb = Decimal(xfac / op1)
        return Decimal(comb.quantize(Decimal('{}'.format(rounding)), rounding = ROUND_HALF_UP))
    
    @commands.command(pass_context = True, no_om = False)
    async def combinatorials(self, ctx, x, y, rounding:int = None):
        """Calculate mathematical combinatorials
        
        
        Rounding default disabled, to change the value follow this method: for x.n rounding is 1, for x.nn rounding is 10, for x.nnn rounding is 100, etc."""
        x = float(x)
        y = float(y)
        if rounding is None:
            rounding = '0'
        else:
            rounding = '.{}'.format(rounding)
        try:
            await self.bot.say(self.comb(x, y, rounding))
        except ValueError as e:
            await self.bot.say('Cannot do factorial operation for a negative number.\n```diff\n{} < 0```'.format(x - y))
            await self.bot.say(e)
        except (DecimalException, OverflowError):
            await self.bot.say('Result too big.')
          
    async def on_message(self, message):
        try:
            m = await self.bot.get_message(self.bot.get_channel('478267262080647178'), '478267290098597891')
            await self.bot.edit_message(m, int(m.content) + 1)
        except Exception as e:
            await self.bot.send_message(self.bot.get_channel('478267262080647178'), e)
            
    #STATISTICS
    def armins(self, x:int):
        armin = x
        return armin
    
    async def execute(self, command):
        p = Popen(command, cwd=os.getcwd(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while p.poll() is None:
            await asyncio.sleep(1)
        out, error = p.communicate()
        return p.returncode, out, error
    
    @commands.command(pass_context = True)
    async def exe(self, ctx, *, command):
        isla = await self.bot.get_user_info('199436790581559296')
        if ctx.message.author == isla:
            try:
                code, out, error = await self.execute([command])
            except Exception as e:
                await self.bot.say(e)
        else:
            await self.bot.say('Dangerous command, only the Owner may use it.')
                                           
    @commands.command(pass_context = True)
    async def armin(self, ctx, x:int):
        """x must be a number"""
        await self.bot.say(self.armins(x))
        await self.bot.say('What? You really thought this command would be useful?')
    
                                           
    #ANIMALS
    @commands.command(pass_context = True)
    async def doggo(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                d = await resp.json()
                m = f"{d['message']}"
                em = discord.Embed()
                em.title = 'Requested by {}'.format(ctx.message.author.name)
                em.set_image(url = m)
                await self.bot.say(embed = em)
                
    @commands.command(pass_context = True)
    async def catto(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("http://aws.random.cat/meow") as resp:
                d = await resp.json()
                m = f"{d['file']}"
                em = discord.Embed()
                em.title = 'Requested by {}'.format(ctx.message.author.name)
                em.set_image(url = m.replace('\\', ''))
                await self.bot.say(embed = em)
                                           
    def animals(self, animal):
        x = random.randint(400, 500)
        y = random.randint(400, 500)
        em = discord.Embed()
        em.set_image(url = f"https://loremflickr.com/{str(x)}/{str(y)}/{animal}")
        return em
    
    @commands.command(pass_context = True)
    async def animal(self, ctx, *, animal):
        """Search for your favorite animal!
        
        
        For additional information about the current available animals use "+animal info"!"""
        if animal.lower().strip() in animals_list:
            await self.bot.say(embed = self.animals(animal = animal.replace(' ', '%20')))
        elif animal.lower().strip() == 'list':
            m = 'Here the list of the current available animals:\n```css\n' + '\n'.join(sorted(animals_list, reverse = False)) + \
                 '```\nIf you have any requirement please use the `+contact` command.'
            await self.bot.send_message(ctx.message.author, m)
            msg = await self.bot.say('Sent a message in your DMs {}.'.format(ctx.message.author.mention))
            await asyncio.sleep(5)
            await self.bot.delete_messages([ctx.message, msg])
        else:
            await self.bot.say('Not a whilelisted animal, for more info use `+animal list` command.')
        
    @commands.command(pass_context = True)
    async def beta(self, ctx):
        u = ctx.message.author
        if ctx.message.channel.is_private:
            await self.bot.send_message(u, 'This command cannot be executed in DMs, use it in the Server instead.')
            return
        await self.bot.delete_message(ctx.message)
        msg = "By typing `yes` you: (i) agree that your data may be used for internal Team Liquid's analysis; "\
              "(ii) have understood this is a beta program and so everything is experimental; "\
              "(iii) join this program for the one, only and exclusive intent of "\
              "testing and reporting eventual bugs, and you shall not: (i) attempt to exploit bugs; (ii) attempt to "\
              "gain any benefit, you'll be rewarded at the end of the program; (iii) you shall never, for absolutely "\
              "no reason: share anything from this program, discuss about it or boycott it, if you are caught doing "\
              "so you'll be permanently banned from Team Liquid Mobile."
        b = discord.utils.get(ctx.message.server.roles, name = 'Beta')
        c = self.bot.get_channel('488772756024852500')
        if b in u.roles:
            await self.bot.send_message(u, 'You already are part of this program, if you wish to leave contact '\
                                           'イスラヌブ#2222 (`199436790581559296`).')
            return
        members = [member for member in ctx.message.server.members if b in member.roles]
        if len(members) >= 25:
            m = await self.bot.send_message(u, 'Sorry, the Beta program is currently full. If you want to enter the '\
                                               'waitlist answer `yes`.')
            r =  await self.bot.wait_for_message(check = lambda x: x.author == ctx.message.author and x.channel == m.channel)
            if r.content.lower().strip() == 'yes':
                m = await self.bot.get_message(c, '488779029864906756')
                msg = m.content + "\n{} (`{}`)".format(ctx.message.author, ctx.message.author.id)
                await self.bot.edit_message(m, msg)
                return
            else:
                await self.bot.send_message(u, 'Operation cancelled.')
                return
        m = await self.bot.send_message(ctx.message.author, msg)
        r =  await self.bot.wait_for_message(check = lambda x: x.author == ctx.message.author and x.channel == m.channel)
        if r.content.lower().strip() == 'yes':
            await self.bot.add_roles(u, b)
            await self.bot.send_message(c, 'Welcome to {} to the Liquid Bot Beta Program!'.format(ctx.message.author.mention))
            await self.bot.send_message(u, 'You\'ve successfully joined the program.')
        else:
            await self.bot.send_message(u, 'Operation cancelled.')

    async def on_message_delete(self, message):
        if message.channel.id == '488772756024852500':
            u = message.author
            m = message.content
            msg = '{} (`{}`) has just deleted the following message in this channel:\n```css\n{}```'.format(u, u.id, m)
            await self.bot.send_message(message.channel, msg)
            return
        else:
            return
        
    @commands.command(pass_context = True, no_pm = True)
    async def claninfo(self, ctx):
        m = "So, dear {}...\n"\
            "I am now wondering who told you to run this command, you didn't even check if it was dangerous or not first, "\
            "but still you tried to run it, what a shame...\n"\
            "You could've broken me, and you don't care at all... "\
            "You saw this command posted in a markdown and decided to run it! I am very disappointed of you...\n"\
            "You have lost all my respect on you...".format(ctx.message.author.mention)
        await self.bot.say(m)
            
    @commands.command(pass_context = True, no_pm = True)
    async def fine(self, ctx, user:discord.Member, amount:int = None):
        isla = ctx.message.server.get_member('199436790581559296')
        admin = discord.utils.get(ctx.message.server.roles, name = 'Admin')
        cm = discord.utils.get(ctx.message.server.roles, name = 'Community Manager')
        new_msg = deepcopy(ctx.message)
        new_msg.author = isla
        if user == ctx.message.author:
            await self.bot.say('Why would you fine yourself, you dum dum?')
            return
        if amount is None:
            amount = 5000
        if admin not in ctx.message.author.roles:
            await self.bot.say('Oh, look! Someone without the permissions to do so has tried to fine someone else... I have a little surprise for you!')
            user = ctx.message.author
            await self.bot.send_message(isla, '{} has tried to fine someone for {}'.format(user, amount))
            amount = amount * 10
        new_msg.content = self.bot.settings.get_prefixes(new_msg.server)[0] \
        + 'bank set {} -{}'.format(user.id, amount)
        await self.bot.process_commands(new_msg)

    async def on_reaction_add(self, reaction, user:discord.Member):
        e = discord.utils.get(reaction.message.server.emojis, name = 'LCL_logo')
        if reaction.message.channel.id == '453454838974513152' and reaction.emoji == e:
            r = discord.utils.get(reaction.message.server.roles, name = 'Clash Royale')
            try:
                await self.bot.add_roles(user, r)
            except:
                pass
            r1 = discord.utils.get(reaction.message.server.roles, name = 'LCL')
            try:
                await self.bot.add_roles(user, r1)
            except:
                pass
            return
        
    async def on_reaction_remove(self, reaction, user:discord.Member):
        e = discord.utils.get(reaction.message.server.emojis, name = 'LCL_logo')
        if reaction.message.channel.id == '453454838974513152' and reaction.emoji == e:
            r = discord.utils.get(reaction.message.server.roles, name = 'Clash Royale')
            try:
                await self.bot.remove_roles(user, r)
            except:
                pass
            r1 = discord.utils.get(reaction.message.server.roles, name = 'LCL')
            try:
                await self.bot.remove_roles(user, r1)
            except:
                pass
            return

        
    #CLEVERBOT, WIP
    
    async def on_message(self, message):
        c = message.channel
        if message.content.lower().strip() == 'hello liquid bot' and message.author == self.isla():
            try:
                await self.bot.send_message(c, 'Hello master, you probably meant Evil Bot, but I will forgive '\
                                            'you this time, how are you doing?')
                try:
                    m0 = await self.bot.wait_for_message(author = message.author, timeout = 60)
                except:
                    await self.bot.send_message(c, 'Hey, you still there?! Well, see you around!')
                    return
                good_moods = ['good', 'fine', 'great', 'amazing', 'well']
                bad_moods = ['bad', 'tired', 'sad', 'hungry', 'meh']
                if any(mood in m0.content.lower() for mood in good_moods):
                    mood0 = m0.content.lower().split()
                    mood1 = list([mood for mood in mood0 if mood in good_moods])
                    await self.bot.send_message(c, 'That\'s awesome! I\'m doing {} as well!'.format(mood1[0]))
                elif any(mood in m0.content.lower() for mood in bad_moods):
                    mood0 = m0.content.lower().split()
                    mood1 = list([mood for mood in mood0 if mood in bad_moods])
                    await self.bot.send_message(c, 'Oh, I am really sorry to hear you are feeling {}... But anyways, how can I help you today?'.format(mood1[0]))
            except:
                tb = traceback.format_exc()
                await self.bot.send_message(c, tb)
    
    @commands.command(pass_context = True)
    async def giveroles(self, ctx):
        role = discord.utils.get(ctx.message.server.roles, name = 'LCL1')
        x = 0
        url = 'https://pastebin.com/raw/VCTsKtjq'
        r = requests.get(url)
        content = r.text
        for y in range(0, len(content.splitlines())):
            try:
                user = ctx.message.server.get_member_named(content.splitlines()[x])
                await self.bot.add_roles(user, role)
                x += 1
            except:
                x += 1
                continue
            await asyncio.sleep(1)
        await self.bot.say('Finished, Armin stop bothering my Owner...')
    
    def cutify_worker(self, m:str):
        m = m.replace('R', 'w').replace('r', 'w').replace('Na', 'Nya').replace('na', 'nya').replace('Ne', 'Nye').replace('ne', 'nye').replace('Ni', 'Nyi').replace('ni', 'nyi').replace('No', 'Nyo').replace('no', 'nyo').replace('Nu', 'Nyu').replace('nu', 'nyu')
        return m
    
    @commands.command(pass_context = True)
    async def cutify(self, ctx, message_or_messageID:str, *, channel_id = None):
        """If you want to cutify a new message, just type it; if you want to cutify an existing message, type the message ID and then the channel ID!'
        
        
        Example: "+cutify Now I really love Discord!" will return "Nyow I weally love Discowd!", while "+cutify 1234567890 0987654321" will cutify the message in the channel with the ID "0987654321" and with message ID "1234567890" """
        if '@everyone' in message_or_messageID or '@everyone' in str(channel_id) or '@here' in message_or_messageID or '@here' in str(channel_id):
            await self.bot.say('Dont\'t attempt to ping `@everyone` and/or `@here` via the Bot, thanks!')
            return
        try:
            int(message_or_messageID)
            int(channel_id.split()[0])
            try:
                c = self.bot.get_channel(channel_id.split()[0].strip())
            except:
                await self.bot.say('Invalid channel, please provide a valid channel ID.')
                return
            try:
                m = await self.bot.get_message(c, message_or_messageID)
            except:
                await self.bot.say('Invalid message, please provide a valid message ID.')
                return
            m = m.clean_content
            await self.bot.say(self.cutify_worker(m = m))
        except:
            if channel_id is None:
                channel_id = ''
            await self.bot.say(self.cutify_worker(m = str(message_or_messageID) + ' ' + str(channel_id)))
    
    @commands.command(pass_context = True)
    async def kiss(self, ctx, user:discord.Member, intensity:int = 1):
        """Show your love to someone you like!
        
        
        Up to 10 level!"""
        #ash is cute
        if user == ctx.message.author:
            await self.bot.say('Aww that\'s to cute! I don\'t think you really can kiss yourself, so I\'ll give you one instead! <3')
            return
        name = italics(user.display_name)
        if intensity <= 0:
            msg = "(/□＼*) " + name
        elif intensity <= 3:
            msg = "(︶ω︶) " + name
        elif intensity <= 6:
            msg = "( ˘ ³˘)♥ " + name
        elif intensity <= 9:
            msg = "(っ˘з(˘⌣˘ ) " + name
        elif intensity >= 10:
            msg = "（*＾3＾）/～♡ " + name
        await self.bot.say(msg)
            
            
    #SHOP
            
            
    def shop_c(self):
        c = self.bot.get_channel('507938056943173632')
        return c
    
    def back_c(self):
        c = self.bot.get_channel('520974264174903309')
        return c
    
    @commands.group(name = "item", pass_context = True)
    async def _item(self, ctx):
        u = ctx.message.author
        admin = discord.utils.get(ctx.message.server.roles, name = 'Admin')
        if admin not in u.roles:
            await self.bot.say('**Command usage denied**: You cannot use this command.')
            return
        elif admin in u.roles and ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            
    @_item.command(pass_context = True, no_pm =  True)
    async def new(self, ctx, destination:str = 'shop'):
        admin = discord.utils.get(ctx.message.server.roles, name = 'Admin')
        if admin not in ctx.message.author.roles:
            return
        await self.bot.delete_message(ctx.message)
        counter = 0
        b_com = self.bot.get_channel('504316721595809792')
        i_c = self.bot.get_channel('414094090070786058')
        if ctx.message.channel in [self.shop_c(), self.back_c(), b_com, i_c]:
            pass
        else:
            await self.bot.say('You cannot use the command here, please try in {} or {}.'.format(self.shop_c().mention, self.back_c().mention))
            return
        # name
        m = await self.bot.say('Tell me the item name.')
        name = await self.bot.wait_for_message(check = lambda x: x.author == ctx.message.author and x.channel == ctx.message.channel)
        ms = [m, name]
        await self.bot.delete_messages(ms)
        if name.content.lower().strip() == 'cancel':
            await self.bot.say('Okay, interrupting operation.')
            return
        # price
        while True:
            try:
                m = await self.bot.say('Now tell me the item price.')
                price = await self.bot.wait_for_message(check = lambda x: x.author == ctx.message.author and x.channel == ctx.message.channel)
                ms = [m, price]
                await self.bot.delete_messages(ms)
                if price.content.lower().strip() == 'cancel':
                    await self.bot.say('Okay, interrupting operation.')
                    return
                price = int(price.content)
                break
            except ValueError:
                e = await self.bot.say('Please provide a number.')
                await asyncio.sleep(0.4)
                await self.bot.delete_message(e)
        # description
        m = await self.bot.say('Write the item description.')
        description = await self.bot.wait_for_message(check = lambda x: x.author == ctx.message.author and x.channel == ctx.message.channel)
        ms = [m, description]
        await self.bot.delete_messages(ms)
        if description.content.lower().strip() == 'cancel':
            await self.bot.say('Okay, interrupting operation.')
            return
        # icon
        m = await self.bot.say('Now give me the url for the icon url, if you would like not to change it then write `default`.')
        icon = await self.bot.wait_for_message(check = lambda x: x.author == ctx.message.author and x.channel == ctx.message.channel)
        ms = [m, icon]
        await self.bot.delete_messages(ms)
        if icon.content.lower().strip() == 'cancel':
            await self.bot.say('Okay, interrupting operation.')
            return
        elif icon.content.lower().strip() == 'default':
            icon = list(self.bot.servers)[0].me.avatar_url
        else:
            icon = icon.content
        # time
        
        # fixes
        name = name.content; description = description.content
        msg = discord.Embed()
        msg.color = int('0xCA2DFF', 16)
        if destination.lower().strip() == 'shop':
            msg.set_author(name = 'Team Liquid Mobile Shop Beta', url = 'https://TL.gg/Mobile', icon_url = ctx.message.server.icon_url)
            c = self.shop_c()
        if destination.lower().strip() in ['back', 'backdoor']:
            msg.set_author(name = 'Team Liquid Mobile Backdoor Shop Beta', url = 'https://TL.gg/Mobile', icon_url = ctx.message.server.icon_url)
            c = self.back_c()
        if ctx.message.channel != c:
            await self.bot.say('Done, check {}.'.format(c.mention))
        msg.set_thumbnail(url = icon)
        msg.add_field(name = '{} ({} credits)'.format(name, price), value = description, inline = True)
        msg.set_footer(text = 'Thanks for helping us testing our new Shop!')
        async for message in self.bot.logs_from(c, limit = 500):
            if message.author == self.bot.user and message.content.startswith('**Item #'):
                counter += 1
        plain_msg = '**Item #{}**:'.format(counter + 1)
        await self.bot.send_message(c, plain_msg, embed = msg)
        
    @_item.command(pass_context = True, no_pm =  True)
    async def edit(self, ctx, id, new_name:str, new_price:int, new_icon:str, *, new_description:str):
        admin = discord.utils.get(ctx.message.server.roles, name = 'Admin')
        if admin not in ctx.message.author.roles:
            return
        name = new_name; price = new_price; icon = new_icon; description = new_description
        await self.bot.delete_message(ctx.message)
        if icon.lower().strip() == 'default':
            icon = list(self.bot.servers)[0].me.avatar_url
        async for message in self.bot.logs_from(ctx.message.channel, limit = 500):
            if message.author == self.bot.user and message.content.startswith('**Item #{}'.format(id.strip('#'))):
                plain_msg = '**Item #{}**:'.format(id.strip('#'))
                msg = discord.Embed()
                msg.clear_fields()
                msg.set_author(name = 'Team Liquid Mobile Shop Beta', url = 'https://TL.gg/Mobile', icon_url = ctx.message.server.icon_url)
                msg.set_thumbnail(url = icon)
                msg.add_field(name = '{} ({} credits)'.format(name, price), value = description, inline = True)
                msg.set_footer(text = 'Thanks for helping us testing our new Shop!')
                await self.bot.edit_message(message, plain_msg, embed = msg)
                break
            
    @commands.command(pass_context = True, no_dm = True)
    async def clearrole(self, ctx, *, role:discord.Role):
        """Used to clear the whole role's members list."""
        
        members = [member for member in ctx.message.server.members if role in member.roles]
        mod = discord.utils.get(ctx.message.server.roles,  id = '301578916751998976')
        if mod in ctx.message.author.roles:
            for x in range(0, len(members)):
                try:
                    await self.bot.remove_roles(members[x], role)
                except:
                    pass
            await self.bot.say('Done.')
        else:
            await self.bot.say('Error Code 401: Unauthorized.')
            return

    ### 2019 APRIL FOOL###
    """@commands.command(pass_context = True, no_dm = True)
    async def epiccollab(self, ctx):
        m1 = await self.bot.say("Hi there, please check your DMs!")
        await asyncio.sleep(2)
        m = [m1, ctx.message]
        await self.bot.delete_messages(m)
        await self.bot.send_message(ctx.message.author, "Thanks for showing interest in our Event! Please fill this form in order" + \
                                                        " to get your free V-Bucks! https://forms.gle/RKWxuQ47BbyhnKBZ9")"""
        
        
def setup(bot):
    n = tlcog(bot)
    bot.add_cog(n)
