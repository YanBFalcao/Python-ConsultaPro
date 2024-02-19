import discord
import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

# TESTE REQUISIÇÃO API
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content == 'regras':
            await message.channel.send(f'{message.author.name} As regras do servidor são: \n 1 - Respeite todos os membros \n 2 - Não ouse falar que a terra é plana!')
        elif message.content == 'nivel':
            await message.author.send(f'Nível 1')
        elif message.content.lower().startswith('cnpj'):
            # Divide a mensagem por espaços e verifica se há pelo menos dois elementos
            message_parts = message.content.split(' ')
            if len(message_parts) < 2:
                await message.channel.send("Formato incorreto. Use 'cnpj' seguido do CNPJ desejado.")
                return

            # Extrai o CNPJ da mensagem
            cnpj = message_parts[1]  # O segundo elemento é o CNPJ

            # Faz a requisição GET para a API com o CNPJ como parâmetro
            api_url = f"https://publica.cnpj.ws/cnpj/{cnpj}"
            response = requests.get(api_url)

            # Verifica se a requisição foi bem sucedida
            if response.status_code == 200:
                data = response.json()
                formatted_data = self.format_data(data)
                print(response.json())
                # Envia apenas a primeira parte dos dados recebidos da API
                partial_data = str(data)[:1500]  # Limita a 1500 caracteres
                # Faça o que deseja com os dados recebidos da API
                await message.channel.send(f"Resultado da pesquisa para o CNPJ {cnpj}: {partial_data}")
            else:
                await message.channel.send(f"Erro ao pesquisar o CNPJ {cnpj}. Tente novamente mais tarde.")

    def format_data(self, data):
        # Formata os dados recebidos da API como uma string
        formatted_data = ""

        # Adiciona as informações desejadas à string formatada
        formatted_data += f"Razão Social: {data['razao_social']}\n"
        formatted_data += f"Capital Social: R$ {data['capital_social']}\n"
        # Adicione mais informações conforme necessário

        return formatted_data

intents = discord.Intents.default()# Ative os intents padrão
intents.members = True

client = MyClient(intents=intents) #Habilitar funcionalidades para membros
client.run('PUT THE TOKEN HERE')