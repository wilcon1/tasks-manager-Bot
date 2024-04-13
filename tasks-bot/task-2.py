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
class task4(commands.Cog):
    def __init__(self,bot) :
        self.bot = bot
    

    @nextcord.slash_command(name="add_task", description="Add a task")
    async def add_task(self, interaction: nextcord.Interaction, id: int, name: str,
                   due_date: str = SlashOption(description="Write time such as 1h left"),
                   priority="Low", description=""):
     cursor.execute("INSERT INTO tasks (id, name, due_date, priority, description, author, assigned_to) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (id, name, due_date, priority, description, interaction.user.name, ""))
     db.commit()
     await interaction.response.send_message(f"Task '{name}' added with ID {id}.")

    @nextcord.slash_command(name="remove_task", description="Remove a task")
    async def remove_task(self, interaction: nextcord.Interaction, task_id: int):
        cursor.execute("SELECT * FROM tasks WHERE id=%s", (task_id,))
        task = cursor.fetchone()
        if task:
            cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
            db.commit()
            await interaction.response.send_message(f"Task '{task['name']}' deleted.")
        else:
            await interaction.response.send_message("Invalid task ID.")






















def setup(bot):
    bot.add_cog(task4(bot))