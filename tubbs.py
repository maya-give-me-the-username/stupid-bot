# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
    async def on_message(self, message):
        # ignore messages from the bot itself
        if message.author == self.user:
            return
        print(f'Message from {message.author}: {message.content}')

        # responses go here
        if message.content.lower() == "67":
            await message.channel.send(f"https://cdn.discordapp.com/attachments/1017962858576883713/1472874359667425310/image0.gif?ex=69c598e4&is=69c44764&hm=a138cea7cb8da5c4b2c483511bedc81a48cdb1b4f87206df66d02ead5603fcae")
        elif message.content.lower() == "ping":
            await message.channel.send("Pong!")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("your-token-here")
