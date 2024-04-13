import nextcord
from nextcord import Interaction
from nextcord.ext import commands, tasks
from nextcord import slash_command, SlashOption
import datetime
import mysql.connector
import os

intents = nextcord.Intents.all()
intents.members = True 
bot = commands.Bot(command_prefix="!", intents=intents)
db = mysql.connector.connect(user="root", host="localhost", database="tasks", password="")
cursor = db.cursor(dictionary=True)

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder.start()

    @tasks.loop(minutes=1)
    async def reminder(self):
        now = datetime.datetime.now()
        cursor.execute("SELECT * FROM tasks WHERE due_date > %s",(now.timestamp(),))
        upcoming_tasks = cursor.fetchall()
        if upcoming_tasks:
            channel = bot.get_channel(1215708476093890600)
            for task in upcoming_tasks:
                await channel.send(f"Reminder: Task '{task['name']}' is due on {task['due_date']}")

    
     
    @nextcord.slash_command(name="clear")
    async def clear(self, interaction: nextcord.Interaction,amount:int):
       await interaction.channel.purge(limit=amount+1)
       await interaction.response.send_message(embed=nextcord.Embed(title="clear",description=f"{amount} messages was deleted"))




    @nextcord.slash_command(name="remove_all_tasks",description="removing all tasks")
    async def remove_all_tasks(self,interaction:Interaction):
     
       task = cursor.fetchall()
       try :
          cursor.execute("DELETE FROM tasks ")
          db.commit()
          await interaction.response.send_message(embed=nextcord.Embed(description="All tasks Have been deleted"))
       except:
          await interaction.response.send_message(embed=nextcord.Embed(description="No tasks avilable to delete"))
    




def setup(bot):
    bot.add_cog(Tasks(bot))
