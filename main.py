import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents = intents)
client.run("MTM2MjgwNTYzMjE1OTE5MTIxMg.Gaq_rx.Qrh5oqLmJSh0vBRfwCMrlzOm0g5pYdQ7x5ekZU")