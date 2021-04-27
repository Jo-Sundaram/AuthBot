import os
import discord

from discord.ext import commands
from discord.utils import get
from util import is_admin, get_student_data, parse_student_data

# Roles
ADMIN_ROLE = "Discordians"
STUDENT_ROLE = "Student"

# Discord Token
TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# Discord API setup

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents)

@client.event
async def on_ready(): 
    """Async function called when the bot first starts and successfully connects to the Discord API
    """
    print(f"We have logged in as {client.user.name}")

@client.event
async def on_message(message):
    """Async function called everytime a message is sent on the Discord server

    Args:
        message (discord.Message): Discord's Message object
    """
    server = message.guild
    discord_key = message.content

    # Ignore bot's own messages
    if message.author == client.user:
        return

    if message.channel.name == "welcome":
        student = get_student_data(discord_key)
        if (student):    
            role = discord.utils.get(server.roles, name=STUDENT_ROLE)
            await message.author.add_roles(role)
            name = student["Preferred name"] if student["Preferred name"] != "" else student["First name"]
            await message.author.edit(nick=name)
        else:
            print(f"Failed to accept {message.author}'s provided key ({discord_key}).")
            
    await client.process_commands(message)

@client.command(name="update")
async def _update(ctx):
    """Async function called when the $update command is used in the Discord server

    Args:
        ctx (context): The context where the command was called from ex. discord.Message
    """
    if is_admin(ctx, ADMIN_ROLE):
        await ctx.send("\> Updating the JSON file!")
        parse_student_data("student_data.csv")
    else:
        await ctx.send("\> You are not authorized to use that command!")


if __name__ == "__main__":
    client.run(TOKEN)
