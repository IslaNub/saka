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
import random
from random import choice, randint
import base64
import json
import aiohttp
import itertools
import requests
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
animals_list = ['tiger', 'bunny', 'rabbit', 'lion', 'cat', 'dog', 'fish', 'snake', 'panda', 'turtle', 'bird', 'bear', 'koala', 'penguin', 'red panda']

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
            await self.bot.say('Cannot do factorial operation for a negative number.\n```py\n{} < 0```'.format(x - y))
            await self.bot.say(e)
        except DecimalException:
            await self.bot.say('Number too big.')
          
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
                em.set_image(url = m)
                await self.bot.say(embed = em)
                                           
    def animals(self, animal):
        x = random.randint(400, 500)
        y = random.randint(400, 500)
        em = discord.Embed()
        em.set_image(url = "https://loremflickr.com/" + str(x) + "/" + str(y) + '/' + animal)
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
              "(ii) have understood this is a beta program and so everything is experimental, we are not responsible "\
              "for any problem this could cause; (iii) join this program for the one, only and exclusive intent of "\
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
        if len(members) == 10:
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
            amount = 50000
        if admin not in ctx.message.author.roles:
            await self.bot.say('Oh, look! Someone without the permissions to do so has tried to fine someone else... I have a little surprise for you!')
            user = ctx.message.author
            await self.bot.send_message(isla, '{} has tried to fine someone for {}'.format(user, amount))
        new_msg.content = self.bot.settings.get_prefixes(new_msg.server)[0] \
        + 'bank set {} -{}'.format(user.id, amount)
        await self.bot.process_commands(new_msg)

    async def on_reaction_add(self, reaction, user:discord.Member):
        e = discord.utils.get(reaction.message.server.emojis, name = 'LCL_logo')
        if reaction.message.channel.id == '453454838974513152' and reaction.emoji == e:
            try:
                r = discord.utils.get(reaction.message.server.roles, name = 'LCL')
                await self.bot.add_roles(user, r)
                await self.bot.send_message(reaction.message.channel, 'Done.')
                return
            except Exception as ex:
                u = reaction.message.server.get_member_named('IslaWoof')
                await self.bot.send_message(reaction.message.channel, ex)
                return
        else:
            u = reaction.message.server.get_member_named('IslaWoof')
            await self.bot.send_message(reaction.message.channel, ex)
            return
        
    async def on_reaction_remove(self, reaction, user:discord.Member):
        e = discord.utils.get(reaction.message.server.emojis, name = 'LCL_logo')
        if reaction.message.channel.id == '453454838974513152' and reaction.emoji == e:
            try:
                r = discord.utils.get(reaction.message.server.roles, name = 'LCL')
                await self.bot.remove_roles(user, r)
                await self.bot.send_message(reaction.message.channel, 'Done.')
                return
            except Exception as ex:
                u = reaction.message.server.get_member_named('IslaWoof')
                await self.bot.send_message(reaction.message.channel, ex)
                return
        else:
            u = reaction.message.server.get_member_named('IslaWoof')
            await self.bot.send_message(reaction.message.channel, ex)
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
    
    
def setup(bot):
    n = tlcog(bot)
    bot.add_cog(n)
