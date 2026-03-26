import discord
from discord import app_commands
import random
import asyncio

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.target_channel_id = None

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.loop.create_task(self.random_pinger())
    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')

        if message.content.lower() == "67":
            await message.channel.send("https://cdn.discordapp.com/attachments/1017962858576883713/1472874359667425310/image0.gif")
        elif message.content.lower() == "ping":
            await message.channel.send(f"{message.author.mention}!")

    async def random_pinger(self):
        await self.wait_until_ready()

        while not self.is_closed():
            if self.target_channel_id is None:
                await asyncio.sleep(5)
                continue

            channel = self.get_channel(self.target_channel_id)

            if channel is None:
                await asyncio.sleep(5)
                continue

            wait_time = random.randint(103, 10000)
            await asyncio.sleep(wait_time)

            members = [m for m in channel.guild.members if not m.bot]
            if not members:
                continue

            target = random.choice(members)
            await channel.send(f"{target.mention} get pinged bastard")

        

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
client = MyClient(intents=intents)

@client.tree.command(name="setchannel", description="Set the ping channel")
async def setchannel(interaction: discord.Interaction, channel: discord.TextChannel):
    client.target_channel_id = channel.id
    await interaction.response.send_message(f"Channel set to {channel.mention}")

@client.tree.command(name="sixseven", description="Send the 67 gif")
async def send_67_gif(interaction: discord.Interaction):
    await interaction.response.send_message("https://cdn.discordapp.com/attachments/1017962858576883713/1472874359667425310/image0.gif")

client.run("your_token_here")
