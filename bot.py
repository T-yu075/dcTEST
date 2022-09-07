import discord
from discord.ext import commands
import os
import json

bot = commands.Bot(command_prefix='!')

with open('./package.json') as jsfile:
    data = json.load(jsfile)
    jsfile.close()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, \
                                   activity=discord.Activity(name='ゆびゆび', \
                                                             type=discord.ActivityType.playing))
    print("Bot is online~")

for file in os.listdir('./cmds'):
    if file.endswith('.py'):
        bot.load_extension(f"cmds.{file[:-3]}")



if __name__=="__main__":
    bot.run(data["token"])

# python bot.py