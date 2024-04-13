import nextcord
from nextcord.ext import commands,tasks
from nextcord import slash_command,SelectOption
import datetime

import os
intens = nextcord.Intents.all()
intens.members = True 
bot = commands.Bot(command_prefix="!",intents=intens)
for filename in os.listdir("./tasks-bot"):
    if filename.endswith(".py"):
        bot.load_extension(f"tasks-bot.{filename[:-3]}")



bot.run("MTIxNjg2NDA4MDU0ODA3MzYzMw.GU8wqP.dYH9hUFTPGJbFEBN3DBsoC0_DF-9hTUMig2oPc")