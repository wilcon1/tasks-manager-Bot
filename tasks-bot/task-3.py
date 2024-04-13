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
class task8(commands.Cog):
    def __init__(self,bot) :
        self.bot = bot

    
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
class task9(commands.Cog):
    def __init__(self,bot) :
        self.bot = bot


    
    @nextcord.slash_command(name="tasks_list", description="List tasks")
    async def tasks_list(self, interaction: nextcord.Interaction):
     cursor.execute("SELECT * FROM tasks")
     tasks = cursor.fetchall()
     if tasks:
        task_list = "\n".join([f"Name: {task['name']}, Due Date: {task['due_date']}, Priority: {task['priority']}" for task in tasks])
        embed = nextcord.Embed(title="Tasks List", description=task_list)
        await interaction.response.send_message(embed=embed)
     else:
        await interaction.response.send_message(embed=nextcord.Embed(description="No tasks available"))
    


    @nextcord.slash_command(name="complete_task",description="completing task thaat you have done")
    async def complete_task(self, interaction: nextcord.Interaction, task_id: int):
     cursor.execute("SELECT * FROM tasks WHERE id=%s", (task_id,))
     task = cursor.fetchone()
    
     if task:
         cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
         db.commit()
         await interaction.response.send_message(f"Task '{task['name']}' completed.")
     else:
         await interaction.response.send_message("Invalid task ID.")






















def setup(bot):
    bot.add_cog(task9(bot))
