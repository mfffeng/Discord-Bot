import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        await message.channel.send(f"You just sent \"{message.content}\".")
        await self.bot.process_commands(message)

    @commands.command(name="Terminate")
    async def terminate(self, ctx):
        self.bot.close()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"The command {ctx.message.content} is invalid!")
            return
        raise error

bot = commands.Bot(command_prefix='!')
bot.add_cog(MyCog(bot))
bot.run(TOKEN)