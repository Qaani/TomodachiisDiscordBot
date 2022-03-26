import os
import random
import discord as py_cord

from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = py_cord.Intents.default()
intents.members = True

bot = py_cord.Bot(intents=intents)


@bot.slash_command(name='hello', description='Say Hello!')  # create a slash command for the supplied guilds
async def hello(ctx):
    """Say hello to the bot"""  # the command description can be supplied as the docstring
    await ctx.respond(f"Hello {ctx.author}!")


@bot.slash_command(
    name="stinks",
    description="Who stinks on the server?",
)
async def stinks(ctx):
    # SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.

    members = ctx.guild.members
    humans = list(filter(lambda m: not m.bot, members))
    randomUser = random.choice(humans)
    await ctx.send(f"{randomUser.mention} stinks")


@bot.slash_command(
    name="chad",
    description="Am I a chad?",
)
async def chad(ctx: py_cord.commands.context.ApplicationContext):
    username = ctx.author.display_name

    if username == "DrPhorkMeh":
        await ctx.send("DrPhorkMeh is the chad")
        await ctx.send("https://media.tenor.com/images/f441bf4d6a7e6329981220844d3b22f7/tenor.gif")
    else:
        await ctx.channel.send(f"{ctx.author} is a loser")

bot.run(DISCORD_TOKEN)
