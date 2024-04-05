import aiohttp
import requests
from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    
    elif 'hello' in lowered:
        return 'Hello There!'
    
    elif 'How are you?' in lowered:
        return 'Goord, Thanks!'
    
    elif 'Bye' in lowered:
        return 'See you!'
    
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    
    elif '15021706000107' in lowered:
        api_url = f"https://publica.cnpj.ws/cnpj/15021706000107"
        response = requests.get(api_url) #Aqui, chama a requisição

        data = response.json() #Aqui, recebe os dados da requisição
        # print(response.json()) // Aqui já consta a consulta realizada.

        partial_data = str(data)[:1500]  #Limita a 1500 caracteres

        return (f"Resultado da pesquisa para o CNPJ {partial_data}")




        # Divide a mensagem por espaços e verifica se há pelo menos dois elementos
        #message_parts = message.content.split(' ')
        #if len(message_parts) < 2:
            # await message.channel.send("Formato incorreto. Use 'cnpj' seguido do CNPJ desejado.")
            # return
            # Extrai o CNPJ da mensagem
            #cnpj = message_parts[1]  # O segundo elemento é o CNPJ

            # api_url = f"https://publica.cnpj.ws/cnpj/{cnpj}"
            # response = requests.get(api_url)
            # async with aiohttp.ClientSession() as session:
            #     async with session.get(api_url) as response:
            #         if response.status == 200:
            #             data = await response.json()
            #             formatted_data = json.dumps(data, indent=2, ensure_ascii=False) # Formatar os dados com indentação e tabela ascii II para visualização de dados com caracteres especiais e acentuações
            #             partial_data = formatted_data[:1500] # Limitar a 1500 caracteres devido a limitação de retorno do discord

            #             # await message.channel.send(f"Resultado da pesquisa para o CNPJ {cnpj}: \n {partial_data}") # Faça o que deseja com os dados recebidos da API
            
            #             with open('dados.json', 'w', encoding='utf-8') as file: #Cria arquivo .json
            #                 json.dump(data, file, ensure_ascii=False, indent=2)
            
            #             with open('dados.json', 'rb') as file:
            #                 await message.channel.send(file=discord.File(file, 'dados.json')) #Envia arquivo JSON para conversa

            #         else:
            #             await message.channel.send(f"Erro ao pesquisar o CNPJ {cnpj}. Tente novamente mais tarde.")

    else:
        return choice(['I do not understante ...',
                       'What are you talking about?',
                       'Do you mindo rephasing that?'])
    