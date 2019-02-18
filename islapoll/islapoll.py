
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
        n = discord.Embed(colour = 0x191970)
        avi = a.avatar_url
        contrast = await self.bot.get_user_info('238598123159683073')
        images = ('https://cdn.shopify.com/s/files/1/1698/6547/files/starcatalog_600x600.jpg?v=1511346010', 'https://wallpapertag.com/wallpaper/middle/7/1/c/544439-best-nighttime-wallpaper-2560x1440-for-phone.jpg', 'https://i.pinimg.com/originals/bc/6e/fc/bc6efc08653224473f590eab54647da4.jpg', 'http://www.newhdwallpaper.in/wp-content/uploads/2014/07/Good-night-time-best-wishes.jpg', 'https://ak5.picdn.net/shutterstock/videos/5633555/thumb/3.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEsvQm_6YaslxY9lOIu5kMXxL174x4PXTwYetByCx70Xqot9uQ')
        image = randchoice(images)
        n.set_thumbnail(url = image)
        n.set_author(name= '{} is going to sleep!'.format(a.name), icon_url=avi)
        if a.id == contrast.id:
            n.description = '{} says good night to all her cute little boys and girls!'.format(a.name)
        else:
            n.description = '{} says good night to all these cute little boys and girls!'.format(a.name)
        n.set_footer(text = 'Good Night!')
        await self.bot.say(embed = n)
        await self.bot.delete_message(ctx.message)
        
    @commands.command(pass_context = True, no_pm = True)
    async def gm(self, ctx):
        a = ctx.message.author
        n = discord.Embed(colour = 0x00BFFF)
        avi = a.avatar_url
        contrast = await self.bot.get_user_info('238598123159683073')
        images = ('https://i.ytimg.com/vi/8Hedq2d1H44/maxresdefault.jpg', 'https://cdn.pixabay.com/photo/2016/08/31/17/41/sunrise-1634197_1280.jpg', 'https://techcrunch.com/wp-content/uploads/2015/10/shutterstock_112249904.jpg', 'https://images.unsplash.com/photo-1504270159110-876cfaca9ece?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=874a6efa6345d66b76fde4099fa67757&w=1000&q=80')
        image = randchoice(images)
        n.set_thumbnail(url = image)
        n.set_author(name= '{} has just woken up!'.format(a.name), icon_url=avi)
        if a.id == contrast.id:
            n.description = '{} says good morning to all her cute little boys and girls!'.format(a.name)
        else:
            n.description = '{} says good morning to all these cute little boys and girls!'.format(a.name)
        n.set_footer(text = 'Good Morning!')
        await self.bot.say(embed = n)
        await self.bot.delete_message(ctx.message)
        
    @commands.command(pass_context = True, no_pm = True)
    async def editchannelperms(self, ctx, role : discord.Role, channel : discord.Channel, read_messages, send_messages, read_message_history):
        """Edit permissions"""
        author = ctx.message.author
        server = ctx.message.server
        rm = read_messages
        sm = send_messages
        rmh = read_message_history
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
        if rmh == 'True':
            overwrite.read_message_history = True
        elif rmh == 'False':
            overwrite.read_message_history = False
        else:
            pass
        mng = discord.utils.get(server.roles, name = 'Managers')
        whitelist = ['200467543968710656', '199436790581559296']
        if author.id in whitelist:
            await self.bot.edit_channel_permissions(channel, role, overwrite)
            if rm != 'True' and rm != 'False':
                rm = 'null'
                pass
            if sm != 'True' and sm != 'False':
                sm = 'null'
                pass
            if rmh != 'True' and rmh != 'False':
                rmh = 'null'
                pass
            await self.bot.say('Edited permissions for {} in {}:\n```Read messages= {}\nSend messages= {}\nRead message history= {}```'.format(role.mention, channel.mention, rm, sm, rmh))
        else:
            await self.bot.say('You can\'t use this command.')

    @commands.command(pass_context = True, no_pm = True)
    async def editchannelpermsglobal(self, ctx, role : discord.Role, read_messages, send_messages, read_message_history):
        """Edit permissions"""
        author = ctx.message.author
        server = ctx.message.server
        rm = read_messages
        sm = send_messages
        rmh = read_message_history
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
        if rmh == 'True':
            overwrite.read_message_history = True
        elif rmh == 'False':
            overwrite.read_message_history = False
        else:
            pass
        mng = discord.utils.get(server.roles, name = 'Managers')
        whitelist = ['200467543968710656', '199436790581559296']
        if author.id in whitelist:
            for channel in server.channels:
                await self.bot.edit_channel_permissions(channel, role, overwrite)
            if rm != 'True' and rm != 'False':
                rm = 'null'
                pass
            if sm != 'True' and sm != 'False':
                sm = 'null'
                pass
            if rmh != 'True' and rmh != 'False':
                rmh = 'null'
                pass
            await self.bot.say('Edited permissions for {} in the whole Server:\n```Read messages= {}\nSend messages= {}\nRead message history= {}```'.format(role.mention, rm, sm, rmh))
        else:
            await self.bot.say('You can\'t use this command.')
            
    async def on_message(self, message):
        u = message.author
        elements = ['Aqueous', 'Aerial', 'Cryogenic', 'Luminous', 'Metallic', 'Thermal', 'Umbral', 'Crystalline']
        c = message.channel
        msg = message.content.strip()
        taboo_violation = ['Singular Unit Detected.', 'ID Tracing.', 'Coordinates Fixed.', 'Report Complete.']
        if msg == 'System Call.':
            sacred_art_start = await self.bot.wait_for_message(check = lambda x: x.author == message.author and x.channel == message.channel, timeout = 30)
            sas = sacred_art_start
            if sas.content.strip().startswith('Generate'):
                command_evok = ['Generate', 'Element.']
                element = re.sub('|'.join(command_evok), '', sas.content).strip()
                if element not in elements:
                    v = 0
                    await asyncio.sleep(0.5)
                    for x in range(0, len(taboo_violation)):
                        warn = await self.bot.send_message(c, taboo_violation[v])
                        await asyncio.sleep(2)
                        await self.bot.delete_message(warn)
                        v += 1
                    await self.bot.delete_messages([message, sas])
            elif sas.content.strip() == 'Inspect Entire Command List':
                if u.id in ['199436790581559296', '173498062260404225']:
                    pass #finish later
                else:
                    v = 0
                    await asyncio.sleep(0.5)
                    await self.bot.send_message(c, 'System Control Authority Required.')
                    await asyncio.sleep(2)
                    for x in range(0, len(taboo_violation)):
                        warn = await self.bot.send_message(c, taboo_violation[v])
                        await asyncio.sleep(2)
                        await self.bot.delete_message(warn)
                        v += 1
                    await self.bot.delete_messages([message, sas])
                    
            
            
def setup(bot):
    n = islapoll(bot)
    bot.add_cog(n)
