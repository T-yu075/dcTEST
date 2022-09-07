import discord
from discord.ext import commands
from core.classes import Cog_
import asyncio
from YTapi.youtubeAPI import channel_viedo_upcoming

class taikida(Cog_):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        async def hisin_tuuchi():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(1003220881092395039)    # 一定要+
            while not self.bot.is_closed():

                url = channel_viedo_upcoming()

                for i in url:
                    await self.channel.send(f"https://www.youtube.com/watch?v={i}")
                    await asyncio.sleep(15)
                # await self.channel.send(f"")
                await asyncio.sleep(600)



        self.bg_task = self.bot.loop.create_task(hisin_tuuchi())

def setup(bot):
    bot.add_cog(taikida(bot))
