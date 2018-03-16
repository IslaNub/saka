import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio
import time

class rsl:
    """Everyone wants saka."""

    def __init__(self, bot):
            self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def who(self, ctx):
        """Find out who is stupid!"""
        channel_id = ctx.message.channel.id
        owner = ctx.message.author
        message = 'Who is stupid?'
        m = await self.bot.send_message(self.bot.get_channel(channel_id), message)
        ms = await self.bot.wait_for_message(check = lambda x : x.author == ctx.message.author)
        IslaNub = '199436790581559296'
        saka = '323543378509824002'
        isla = '<@199436790581559296>'
        if ctx.message.author.id == IslaNub:
            await self.bot.say(f'Oh, my Master! You\'re the brightest person I\'ve ever seen! You definitely are right! {ms.content} really is stupid!')
        elif ctx.message.author.id == saka:
            await self.bot.say(f'Awww saka, since Isla has faith in you I\'m pretty sure you\'re right, {ms.content} is pretty much stupid!')
        elif ms.content == isla:
            await self.bot.say('Idk')
        else:
            await self.bot.say('Are you sure? (yes/no)')
            answer1 = ('yes')
            answer2 = ('no')
            msg = await self.bot.wait_for_message(author=owner)
            if msg.content.lower().strip() in answer1:
                if ms.content == 'I':
                    await self.bot.send_message(self.bot.get_channel(channel_id), 'Indeed, you are! Btw it\'s "me", not "I"...')
                elif ms.content == 'You':
                    await self.bot.send_message(self.bot.get_channel(channel_id), 'I am smart enough to understand you tried to troll me... Believe me, the stupid here is you, not me!')
                else:
                    await self.bot.send_message(self.bot.get_channel(channel_id), f'Hmm perhaps, I\'m not sure if {ms.content} is stupid, but I\'m sure YOU are!')
            elif msg.content.lower().strip() in answer2:
                await self.bot.send_message(self.bot.get_channel(channel_id), 'Nice! You\'re right, because you\'re stupid!')
            else:
                await self.bot.send_message(self.bot.get_channel(channel_id), 'What don\'t you understand of "yes/no"??? Look how stupid...')
    
    @commands.command(pass_context=True, no_pm=True)
    async def newbot(self, ctx):
        IslaNub = '199436790581559296'
        if ctx.message.author.id == IslaNub:
            channel_id = '390057135905570817'
            announcements = '<#390057135905570817>'
            await self.bot.send_message(self.bot.get_channel(channel_id), '\nI\'m your new bot! Soon I\'ll bring games and utility stuff in the Server!\n`Beep boop`')
            await self.bot.say(f'Message sent in {announcements}.')
        else:
            await self.bot.say('Command Access Denied.')

    @commands.group(pass_context=True, no_pm=True)
    async def rsl(self, ctx):
        """RSL UTILITY COMMANDS"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @commands.has_permissions(administrator = True)
    @rsl.command(pass_context = True, name = 'announce')
    async def rsl_announce(self, ctx, *, msg):
        """Send message in #announcements
        
        +rsl announce <message>"""
        channel_id = '390057135905570817'
        await self.bot.send_message(self.bot.get_channel(channel_id), msg)
        announcements = '<#390057135905570817>'
        await self.bot.say(f'Message sent in {announcements}')

    @commands.command(pass_context = True, no_pm = True)
    async def witch(self, ctx, member):
        """Wow look! A b... witch!"""
        await self.bot.say(f'{member} is a __w__itch!')
        await self.bot.say(type(ctx.message.author.id))

    @rsl.command(pass_context = True, name = 'signup')
    async def rsl_signup(self, ctx, user: discord.Member = None):
        """Sends sign-up form in DM"""
        if user is None:
            u = ctx.message.author
            m = 'https://docs.google.com/forms/d/e/1FAIpQLSdQws_E_lBjGeZisIE8zUK54sIVBO6hitdRwiLOVZI_b_tP-g/viewform'
            await self.bot.send_message(u, m)
            await self.bot.say(f'Sign-up form sent in DM to {u.mention}.')
        elif ctx.message.author.server_permissions.administrator:
            m = 'https://docs.google.com/forms/d/e/1FAIpQLSdQws_E_lBjGeZisIE8zUK54sIVBO6hitdRwiLOVZI_b_tP-g/viewform'
            await self.bot.send_message(user, m)
            await self.bot.say(f'Sign-up form sent in DM to {user.mention}.')
        else:
            await self.bot.say('You don\'t have permissions to send the sign-up form in DM via the Bot.')

    @commands.has_permissions(administrator = True)
    @rsl.command(pass_context = True, name = 'purge')
    async def rsl_purge(self, ctx):
        """⚠⚠⚠!!!Deletes bunch of messages!!!⚠⚠⚠"""
        channel_id = ctx.message.channel.id
        deleted = await self.bot.purge_from(self.bot.get_channel(channel_id), limit=1000, check=None, before=None, around=None)
        await self.bot.send_message(self.bot.get_channel(channel_id), 'Deleted {} messages'.format(len(deleted)))
        
    async def on_member_join(self, member):
        recruitment = '<#408205979805548545>'
        m = f'Welcome {member.mention} to Royal Smash League.\n\n**First off lets get your roles registered.**\n\n- To get a Captain role (only for team captains), please type: `+selfrole Captain`\n- To get any of the Region roles, please type: `+selfrole Region_NA` or `+selfrole Region_APAC` or `+selfrole Region_EU`\n- To get a Graphics Designer role, please type: `+selfrole GFX Designer`\n\n**Once you have done all that you\'re now onto getting your team registered for the next season.**\n\n- To register for the next season, please type: `+rsl signup`\n- You will get a form sent to your DMs you don\'t need to instantly fill out the form straight away, it will not disappear or close until one of the Directors make an announcement, and even then they will be sure to give 1-2 weeks advance on the dead line.\n\n**Now if you\'re looking for a team.**\n\n- You can access {recruitment} channel in our server, which is under the category "Clash Royale", and there you can find all the current teams that are recruiting for members at that time.\n\nGood Luck with your time in RSL we hope to hear from you again.'
        await self.bot.send_message(member, m)

    @rsl.command(pass_context = True, name = 'welcome')
    async def rsl_welcome(self, ctx, user: discord.Member = None):
        """Sends the welcome message

        If there's no mention then sends the message to the author"""
        recruitment = '<#408205979805548545>'
        member = ctx.message.author
        if user is None:
            author = ctx.message.author
            m = f'Welcome {member.mention} to Royal Smash League.\n\n**First off lets get your roles registered.**\n\n- To get a Captain role (only for team captains), please type: `+selfrole Captain`\n- To get any of the Region roles, please type: `+selfrole Region_NA` or `+selfrole Region_APAC` or `+selfrole Region_EU`\n- To get a Graphics Designer role, please type: `+selfrole GFX Designer`\n\n**Once you have done all that you\'re now onto getting your team registered for the next season.**\n\n- To register for the next season, please type: `+rsl signup`\n- You will get a form sent to your DMs you don\'t need to instantly fill out the form straight away, it will not disappear or close until one of the Directors make an announcement, and even then they will be sure to give 1-2 weeks advance on the dead line.\n\n**Now if you\'re looking for a team.**\n\n- You can access {recruitment} channel in our server, which is under the category "Clash Royale", and there you can find all the current teams that are recruiting for members at that time.\n\nGood Luck with your time in RSL we hope to hear from you again.'
            await self.bot.send_message(author, m)
            await self.bot.say(f'Sent the welcome message in DM to {author.mention}.')
        elif ctx.message.author.server_permissions.administrator:
            m = f'Welcome {user.mention} to Royal Smash League.\n\n**First off lets get you\'re roles registered.**\n\n- To get a Captain role (only for team captains), please type: `+selfrole Captain`\n- To get any of the Region roles, please type: `+selfrole Region_NA` or `+selfrole Region_APAC` or `+selfrole Region_EU`\n- To get a Graphics Designer role, please type: `+selfrole GFX Designer`\n\n**Once you have done all that you\'re now onto getting your team registered for the next season.**\n\n- To register for the next season, please type: `+rsl signup`\n- You will get a form sent to your DMs you don\'t need to instantly fill out the form straight away, it will not disappear or close until one of the Directors make an announcement, and even then they will be sure to give 1-2 weeks advance on the dead line.\n\n**Now if you\'re looking for a team.**\n\n- There is an easy to access\n{recruitment} channel in our server, it in under the category of "Clash Royale", and there you can find all the current teams that are recruiting for members at that time.\n\nGood Luck with your time in RSL we hope to hear from you again.'
            await self.bot.send_message(user, m)
            await self.bot.say(f'Sent the welcome message in DM to {user.mention}.')
        else:
            await self.bot.say('You don\'t have permissions to send the welcome message in DM via the Bot.')

    @rsl.command(pass_context = True, name='bans')
    async def get_bans(self, ctx, server: discord.Server = None):
        """Gets bans"""
        server = ctx.message.server.id
        await self.bot.say(self.bot.get_bans(server))
        return

    @rsl.command(pass_context = True, no_pm = True, name = 'rosterchange')
    async def rsl_rosterchange(self, ctx):
        """Allows you to change your roster"""
        channel_id = '422335220784824331'
        c = self.bot.get_channel(channel_id)
        u = ctx.message.author
        cap = discord.utils.get(ctx.message.server.roles, name = 'Captain')
        if cap in u.roles:
            yesanswer = ('yes')
            q1 = await self.bot.say('Write in chat your Team Name.')
            a1 = await self.bot.wait_for_message(author = u)
            q2 = await self.bot.say('Now write in chat the players you want to add, separate them with a `;`.')
            a2 = await self.bot.wait_for_message(author = u)
            q3 = await self.bot.say('Now write in chat the players you want to remove, separate them with a `;`.')
            a3 = await self.bot.wait_for_message(author = u)
            q4 = await self.bot.say('Are you sure about this changes? (yes/no)')
            a4 = await self.bot.wait_for_message(author = u)
            if a4.content.lower().strip() in yesanswer:
                em = discord.Embed()
                em.title = f'Roster changes from {ctx.message.author.name} ({a1.content})'
                em.color = 0x3094F4
                em.description = f'**__Team Name:__**\n{a1.content}\n\n**__Added Players:__**\n{a2.content}\n\n**__Removed players:__**\n{a3.content}'
                messages = (q1, q2, q3, q4, a1, a2, a3, a4)
                await self.bot.delete_messages(messages)
                await self.bot.send_message(c, embed = em),
                await self.bot.say('Sent roster changes to our Staff.')
            else:
                await self.bot.say('Operation canceled.')
        else:
            await self.bot.say('Only Team Captains can change the roster.')

    @commands.command(pass_context=True, no_pm=True)
    async def stream(self, ctx, *, message):
        """Send your stream information to Staff."""
        channel_id = '412304061761585152'
        c = self.bot.get_channel(channel_id)
        em = discord.Embed()
        em.title = f'Stream informations from "{ctx.message.author.name}"'
        em.color = 0x3094F4
        em.description = message
        u = ctx.message.author
        cas = discord.utils.get(ctx.message.server.roles, name = 'CASTERS')
        if cas in u.roles:
            await self.bot.send_message(c, embed = em)
            await self.bot.say('Stream information sent to our Staff.')
        else: 
            await self.bot.say('Only Casters can send Stream Informations.')

def setup(bot):
    bot.add_cog(rsl(bot))