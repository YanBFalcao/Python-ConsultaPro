import discord

intents = discord.Intents.default()# Ative os intents padrão

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith('regras'):
            await message.channel.send(f'{message.author.name} As regras do servidor são: \n 1 - Respeite todos os membros \n 2 - Não ouse falar que a terra é plana!')

client = MyClient(intents=intents)
client.run('token here')