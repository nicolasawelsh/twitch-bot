import os
from twitchio.ext import commands
from datetime import datetime
from pytz import timezone

from get_commands import commands_dict

# pipenv run python bot.py


bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has joined!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")


@bot.command(name="betterttv")
async def betterttv(ctx):
    command = commands_dict.get("betterttv")
    if command is not None:
        await ctx.send(command)


@bot.command(name="catjam")
async def catjam(ctx):
    command = commands_dict.get("catjam")
    if command is not None:
        await ctx.send(command)


@bot.command(name="catjamultra")
async def catjamultra(ctx):
    command = commands_dict.get("catjamultra")
    if command is not None:
        await ctx.send(command)


@bot.command(name="discord")
async def discord(ctx):
    command = commands_dict.get("discord")
    if command is not None:
        await ctx.send(command)


@bot.command(name="donate")
async def donate(ctx):
    command = commands_dict.get("donate")
    if command is not None:
        await ctx.send(command)


@bot.command(name="frog")
async def frog(ctx):
    command = commands_dict.get("frog")
    await ctx.send(command)


@bot.command(name="games")
async def games(ctx):
    command = commands_dict.get("games")
    if command is not None:
        await ctx.send(command)


@bot.command(name="loc")
async def loc(ctx):
    command = commands_dict.get("loc")
    if command is not None:
        await ctx.send(command)


@bot.command(name="lurk")
async def lurk(ctx):
    command = commands_dict.get("lurk")
    if command is not None:
        await ctx.send(ctx.author.name + command)


@bot.command(name="rules")
async def rules(ctx):
    command = commands_dict.get("rules")
    if command is not None:
        await ctx.send(command)


@bot.command(name="shoutout")
async def shoutout(ctx, arg):
    command = commands_dict.get("shoutout")
    if command is not None:
        await ctx.send(command[0] + arg + command[1] + arg)


@bot.command(name="specs")
async def specs(ctx):
    command = commands_dict.get("specs")
    if command is not None:
        await ctx.send(command)


# @bot.command(name="time")
# async def time(ctx):
#     command = commands_dict.get("time")
#     curr_time = datetime.now(command[1])
#     await ctx.send(command[0] + curr_time + " " + command[1])


if __name__ == "__main__":
    bot.run()
