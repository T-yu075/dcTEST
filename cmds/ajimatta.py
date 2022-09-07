import discord
from discord.ext import commands
from core.classes import Cog_
import asyncio
from YTapi.youtubeAPI import channel_viedo_live

class ajimaru(Cog_):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        async def hisin_ajimatta():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(1003220881092395039)    # 一定要+
            while not self.bot.is_closed():
                print("Hello!")
                y = channel_viedo_live()

                # await self.channel.send(y)
                print(y)
                await asyncio.sleep(30)

        # self.bg_task = self.bot.loop.create_task(hisin_ajimatta())

def setup(bot):
    bot.add_cog(ajimaru(bot))
