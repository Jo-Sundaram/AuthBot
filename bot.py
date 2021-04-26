import os
import discord

from discord.ext import commands
from discord.utils import get
from util import is_admin, parse_student_info, get_student_info

# Roles
ADMIN_ROLE = "discordians"
STUDENT_ROLE = "Student"

# Discord Token
TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# Discord API setup
# https://discordpy.readthedocs.io/en/latest/api.html?highlight=intent#discord.Intents
intents = discord.Intents.all()
 # https://discordpy.readthedocs.io/en/latest/api.html?highlight=client#discord.Client
client = commands.Bot(command_prefix="$ ", intents=intents)


# https://discordpy.readthedocs.io/en/latest/api.html?highlight=on_ready#discord.on_ready
@client.event
async def on_ready(ctx):
    # student_role = await guild.create_role(
    #     name=f"Group: {group}", mentionable=True
    # )

    print(f"We have logged in as {client}")


# https://discordpy.readthedocs.io/en/latest/api.html?highlight=on_message#discord.on_message
@client.event
async def on_message(message):
    student_role = discord.utils.get(guild.roles, name=STUDENT_ROLE)
    discord_key = message.content

    # Ignore bot's own messages
    if message.author == client.user:
        return

    if message.channel.name == "welcome":
        if discord_key in student_data:
            student = get_student_info(discord_key)
            role = get(guild.roles, name=STUDENT_ROLE)
            await message.author.add_roles(role)
            message.author.name = student["Preferred Name"]

    await client.process_commands(message)


# ctx = https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=context#discord.ext.commands.Context
@client.command(name="!hello")
async def _hello(ctx):
    if is_admin(ctx, ADMIN_ROLE):
        await ctx.send("\> Hello!")
    else:
        await ctx.send("\> You are not authorized to use that command!")


if __name__ == "__main__":
    client.run(TOKEN)
