from telethon.sync import TelegramClient

"""
This file get message from a group and return them
"""

class return_messages:
    def __init__(self, api_id, api_hash): #Define api id and hash
        self.api_id = api_id
        self.api_hash = api_hash


    def get_all(self, group_link):
        """
        This return the message sent in sender group
        """
        with TelegramClient('login', self.api_id, self.api_hash) as client:
            for z in client.get_messages(group_link): #Get the last message sent
                return z.text


