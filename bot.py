from twitchio.ext import commands
from datetime import datetime
from pytz import timezone

from get_commands import commands_dict
from get_commands import connection_dict


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=connection_dict.get("irc_token"),
                         client_id=connection_dict.get("client_id"),
                         nick=connection_dict.get("nick"),
                         prefix=connection_dict.get("prefix"),
                         initial_channels=[connection_dict.get("initial_channels")])

    async def event_ready(self):
        print(f"{self.nick} is online!")
        ws = bot._ws
        await ws.send_privmsg(self.initial_channels[0], f"/me has joined!")

    async def event_message(self, ctx):
        # ignores itself and the streamer
        if ctx.author.name.lower() == self.nick.lower():
            return

        await bot.handle_commands(ctx)

        if 'hello' in ctx.content.lower():
            await ctx.channel.send(f"Hi, @{ctx.author.name}!")

    @commands.command(name="betterttv")
    async def betterttv(self, ctx):
        command = commands_dict.get("betterttv")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="catjam")
    async def catjam(self, ctx):
        command = commands_dict.get("catjam")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="catjamultra")
    async def catjamultra(self, ctx):
        command = commands_dict.get("catjamultra")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="discord")
    async def discord(self, ctx):
        command = commands_dict.get("discord")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="donate")
    async def donate(self, ctx):
        command = commands_dict.get("donate")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="frog")
    async def frog(self, ctx):
        command = commands_dict.get("frog")
        await ctx.send(command)

    @commands.command(name="games")
    async def games(self, ctx):
        command = commands_dict.get("games")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="loc")
    async def loc(self, ctx):
        command = commands_dict.get("loc")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="lurk")
    async def lurk(self, ctx):
        command = commands_dict.get("lurk")
        if command is not None:
            await ctx.send(ctx.author.name + command)

    @commands.command(name="rules")
    async def rules(self, ctx):
        command = commands_dict.get("rules")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="shoutout")
    async def shoutout(self, ctx, arg):
        command = commands_dict.get("shoutout")
        if command is not None:
            await ctx.send(command[0] + arg + command[1] + arg)

    @commands.command(name="specs")
    async def specs(self, ctx):
        command = commands_dict.get("specs")
        if command is not None:
            await ctx.send(command)

    @commands.command(name="youtube")
    async def youtube(self, ctx):
        command = commands_dict.get("youtube")
        if command is not None:
            await ctx.send(command)

# @commands.command(name="time")
# async def time(self, ctx):
#     command = commands_dict.get("time")
#     curr_time = datetime.now(command[1])
#     await ctx.send(command[0] + curr_time + " " + command[1])


bot = Bot()
bot.run()
