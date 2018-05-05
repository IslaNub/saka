@commands.group(pass_context=True, no_pm=True)
    async def buy(self, ctx):
        """Buy stuff from the Shop"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

@buy.command(pass_context = True, no_pm = True, name = test)
async def _test(self, ctx):
    try:
        user = ctx.message.author
        server = ctx.message.server
        self.bank.withdraw_credits(user, credits.sum)
        logger.info("Removed {} credits to {} ({})".format(credits.sum, user.name, user.id))
        role = discord.utils.get(server.roles, name = 'test')
        await self.bot.add_roles(user, role)
        await self.bot.say('You\'ve successfully bought *{}* role for {} credits!'.format(role.name, credits.sum))

            
    except InsufficientBalance:
        await self.bot.say("User doesn't have enough credits.")
    except NoAccount:
        await self.bot.say("User has no bank account.")
