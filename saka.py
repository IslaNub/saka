import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio
import time

class saka:
    """Everyone wants saka."""

    def __init__(self, bot):
            self.bot = bot

    @commands.group(pass_context=True, no_pm=True)
    async def saka(self, ctx):
        """Do you really love saka?"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @saka.command(pass_context=True, name= 'love')
    async def saka_love(self, ctx):
        """Use if you really love saka... Oh only Isla can..."""
        owner = ctx.message.author
        IslaNub = '199436790581559296'
        saka = '323543378509824002'
        channel_id = ctx.message.channel.id
        message = 'Say "Yes" if you do, say "No" if you don\'t.'
        m = await self.bot.send_message(self.bot.get_channel(channel_id), message)
        msg = await self.bot.wait_for_message(author=owner, timeout=15)
        answer1 = ('yes')
        answer2 = ('no')
        if msg.content.lower().strip() in answer1:
            if ctx.message.author.id == IslaNub:
                mes = 'I LOVE YOU SAKA! :`:<:GWnanamiSachiHeart:407618557636116481>:`:'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '💕')
            elif ctx.message.author.id == saka:
                mes = 'Saka:`:<:lovepanda:412287195496448010>:`:Isla'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '💞')
            else:
                mes = 'Don\'t dare to do it again... :`:<:GWnanaREEEEEEEEEE:392308452208410627>:`:'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '☠')
        elif msg.content.lower().strip() in answer2:
            if ctx.message.author.id == IslaNub:
                mes = 'Just kidding, he loves saka! :`:<:GWnanamiSachiHeart:407618557636116481>:`:'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '💕')
            elif ctx.message.author.id == saka:
                mes = 'Well, all I know is:\nSaka:`:<:lovepanda:412287195496448010>:`:Isla'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '💞')
            else:
                mes = 'As much only Isla can have saka you must love him too! :`:<:GWnanaREEEEEEEEEE:392308452208410627>:`:'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '☠')
        elif msg.content.lower().strip() not in answer1 and msg.content.lower().strip() not in answer2:
            if ctx.message.author.id == IslaNub:
                mes = 'No matter the answer, everyone knows he does! :`:<:GWnanamiSachiHeart:407618557636116481>:`:'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '💕')
            elif ctx.message.author.id == saka:
                mes = 'Whichever the answer is:\nSaka:`:<:lovepanda:412287195496448010>:`:Isla'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '💞')
            else:
                mes = 'What don\'t you understand of "Say "Yes" if you do, say "No" if you don\'t"?! :`:<:GWnanaREEEEEEEEEE:392308452208410627>:`:'
                await self.bot.edit_message(m, mes)
                await self.bot.add_reaction(ctx.message, '☠')
        else:
            pass

    @commands.command(pass_context=True)
    async def party(self, ctx):
        """Oh yeah, let's freaking party!"""
        IslaNub = '199436790581559296'
        saka = '323543378509824002'
        if ctx.message.author.id == IslaNub:
            await self.bot.say(':`:<a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112>:`:')
        elif ctx.message.author.id == saka:
            await self.bot.say(':`:<a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112><a:partytrain:404395160101978112>:`:')
        else:
            await self.bot.say(':`:<a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240><a:ablobowo:403607533803274240>:`:')

    @commands.command(pass_context=True)
    async def test1(self, ctx):
        """Just a test, can't you read the name??? :/"""
        channel_id = '420270325788311564'
        message = '@here\nTest1'
        await self.bot.send_message(self.bot.get_channel(channel_id), message)

def setup(bot):
    bot.add_cog(saka(bot))
