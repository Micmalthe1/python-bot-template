import discord
from discord import app_commands


TOKEN = ''

intents = discord.Intents.default()
intents = discord.Intents.all()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

class bot(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=intents)
        self.synced=False
    async def on_ready(self):
        await self.wait_until_ready()
        await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Game(f'Made By michal & Noah | bot is in {len(bot.guilds)} servers')
        )
        print(f"{bot.user.name} is online")

bot = bot()
tree = app_commands.CommandTree(bot)
tree.remove_command("help")


@tree.command(name="ping", description="🏓")
async def sync(ctx: discord.Interaction):
    ctx.response.send_message("Pong!")

