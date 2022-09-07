from discord.ext import commands


class Cog_(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel = self.bot.get_channel(1003220881092395039)    # 可以甭(?

def setup(bot):
    bot.add_cog(Cog_(bot))