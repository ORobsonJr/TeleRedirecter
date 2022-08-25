from telethon.sync import TelegramClient

"""
This file is used to send message to other telegram group
"""

class send_message:
    def __init__(self, api_id, api_hash): #Define id and hash from API
        self.api_id = api_id 
        self.api_hash = api_hash
        
    def send_to(self,message, group_link):
        """
        This send a message to target group by a selected message
        """
        try: 
            with TelegramClient('login', self.api_id, self.api_hash) as client: #Create connection
                entity=client.get_entity(group_link) #Get entity from the target group. It's required in telegram API
                client.send_message(entity=entity,message=message) #Sent message to target gruoup
                print('[*]MESSAGE {MESSAGE} SENT'.format(MESSAGE=message)) 


        except Exception as e:
            print('[ERROR]: ', e)    
   

