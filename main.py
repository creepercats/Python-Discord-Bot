import discord
from dotenv import dotenv_values

config = dotenv_values(".env")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.all()

client = MyClient(intents=intents)
client.run(config.get("DISCORD_KEY"))

