from telethon import TelegramClient


class GET():
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash

    def get_id(self, sender_link: str = '', receiver_link: str = ''):
        with  TelegramClient('login', self.api_id, self.api_hash) as client:
            final_value = {'receiver': 0, 'sender': 0} #Get entity from 
            ids_group = [] #List that store ids from groups


            if sender_link and receiver_link:
                for metadata in client.iter_dialogs():
                    if metadata.name == sender_link:
                        final_value['receiver'] = metadata.id

                    elif metadata.name == receiver_link:
                        final_value['sender'] = metadata.id

                    return final_value

            else:               
                for number, metadata in enumerate(client.iter_dialogs()):
                    ids_group.append(metadata.id)
                    print(f'[{number}]', metadata.name)

                mode = int(input('Digite o número do grupo que vai receber menssagens(grupo alvo): '))
                final_value['receiver'] = ids_group[mode]

                mode = int(input('Digite o número do grupo que vai enviar menssagens(grupo enviador): '))
                final_value['sender'] = ids_group[mode]

                return final_value





    