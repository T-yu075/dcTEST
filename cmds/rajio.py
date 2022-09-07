import discord
from discord.ext import commands
from core.classes import Cog_
import asyncio
import datetime


class timeTask(Cog_):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # async def interval():
        #     # pass
        #     print("Run interval")
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(1003220881092395039)
        #     while not self.bot.is_closed():
        #         await self.channel.send("ぉぁょ~")
        #         await asyncio.sleep(5)
        # self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(1003220881092395039)    # 一定要+
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%H:%M")
                weekk = datetime.datetime.today().isoweekday()

                if weekk == 7 and now_time == "15:59":
                    await self.channel.send(f"準備聽廣播啦~\nhttps://www.uniqueradio.jp/agplayer5/player.php")
                    await asyncio.sleep(60)
                else:
                    await asyncio.sleep(60)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

def setup(bot):
    bot.add_cog(timeTask(bot))
