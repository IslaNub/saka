    async def on_member_join(self, member):
        recruitment = '<#408205979805548545>'
        m = f'Welcome {member.mention} to Royal Smash League.\n\n**First off lets get you\'re roles registered.**\n\n- To get a Captain role (only for team captains), please type: `+selfrole Captain`\n- To get any of the Region roles, please type: `+selfrole Region_NA` or `+selfrole Region_APAC` or `+selfrole Region_EU`\n- To get a Graphics Designer role, please type: `+selfrole GFX Designer`\n\n**Once you have done all that you\'re now onto getting your team registered for the next season.**\n\n- To register for the next season, please type: `+rsl signup`\n- You will get a form sent to your DMs you don\'t need to instantly fill out the form straight away, it will not disappear or close until one of the Directors make an announcement, and even then they will be sure to give 1-2 weeks advance on the dead line.\n\n**Now if you\'re looking for a team.**\n\n- There is an easy to access\n{recruitment} channel in our server, it in under the category of "Clash Royale", and there you can find all the current teams that are recruiting for members at that time.\n\nGood Luck with your time in RSL we hope to hear from you again.'
        await self.bot.send_message(member, m)

    @rsl.command(pass_context = True, name = 'welcome')
    async def rsl_welcome(self, ctx, user: discord.Member = None):
        """Sends the welcome message

        If there's no mention then sends the message to the author"""
        recruitment = '<#408205979805548545>'
        member = ctx.message.mentions
        if user is None:
            author = ctx.message.author
            m = f'Welcome {author.mention} to Royal Smash League.\n\n**First off lets get you\'re roles registered.**\n\n- To get a Captain role (only for team captains), please type: `+selfrole Captain`\n- To get any of the Region roles, please type: `+selfrole Region_NA` or `+selfrole Region_APAC` or `+selfrole Region_EU`\n- To get a Graphics Designer role, please type: `+selfrole GFX Designer`\n\n**Once you have done all that you\'re now onto getting your team registered for the next season.**\n\n- To register for the next season, please type: `+rsl signup`\n- You will get a form sent to your DMs you don\'t need to instantly fill out the form straight away, it will not disappear or close until one of the Directors make an announcement, and even then they will be sure to give 1-2 weeks advance on the dead line.\n\n**Now if you\'re looking for a team.**\n\n- There is an easy to access\n{recruitment} channel in our server, it in under the category of "Clash Royale", and there you can find all the current teams that are recruiting for members at that time.\n\nGood Luck with your time in RSL we hope to hear from you again.'
            await self.bot.send_message(author, m)
            await self.bot.say(f'Sent the welcome message in DM to {author.mention}.')
        else:
            m = f'Welcome {user.mention} to Royal Smash League.\n\n**First off lets get you\'re roles registered.**\n\n- To get a Captain role (only for team captains), please type: `+selfrole Captain`\n- To get any of the Region roles, please type: `+selfrole Region_NA` or `+selfrole Region_APAC` or `+selfrole Region_EU`\n- To get a Graphics Designer role, please type: `+selfrole GFX Designer`\n\n**Once you have done all that you\'re now onto getting your team registered for the next season.**\n\n- To register for the next season, please type: `+rsl signup`\n- You will get a form sent to your DMs you don\'t need to instantly fill out the form straight away, it will not disappear or close until one of the Directors make an announcement, and even then they will be sure to give 1-2 weeks advance on the dead line.\n\n**Now if you\'re looking for a team.**\n\n- There is an easy to access\n{recruitment} channel in our server, it in under the category of "Clash Royale", and there you can find all the current teams that are recruiting for members at that time.\n\nGood Luck with your time in RSL we hope to hear from you again.'
            await self.bot.send_message(user, m)
            await self.bot.say(f'Sent the welcome message in DM to {user.mention}.')

                @rsl.command(pass_context = True, name = 'signup')
    async def rsl_signup(self, ctx, user: discord.Member = None):
        """Sends sign-up form in DM"""
        if user is None:
            u = ctx.message.author
            m = 'https://docs.google.com/forms/d/e/1FAIpQLSdQws_E_lBjGeZisIE8zUK54sIVBO6hitdRwiLOVZI_b_tP-g/viewform'
            await self.bot.send_message(u, m)
            await self.bot.say(f'Sign-up form sent in DM to {u.mention}.')
        elif ctx.message.author.has_permission(administrator):
            m = 'https://docs.google.com/forms/d/e/1FAIpQLSdQws_E_lBjGeZisIE8zUK54sIVBO6hitdRwiLOVZI_b_tP-g/viewform'
            await self.bot.send_message(user, m)
            await self.bot.say(f'Sign-up form sent in DM to {user.mention}.')
