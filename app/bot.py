from get_messages import return_messages
from send_message import send_message
from get_id_group import GET


class bot:
    def __init__(self, receiver, sender ):
        self.receiver = receiver
        self.sender = sender

    def _main_(self):
        while True:            
            last_message = [] #Store the last message received
            value = 0
            while True:
                message = return_messages.get_all(group_link=self.receiver) #Get the message 
                try:
                    last_message.index(message) #This is used to avoid loop problems
                    value = 1

                except ValueError:
                     last_message.append(message)
                     value = 0
                     
                if message != None:
                    if value == 0:
                        print('Menssagem recebida: ', message)
                        send_message.send_to(message=message, group_link=self.sender)



            

if __name__ == '__main__':
    group_id = {'receiver': -785419607, 'sender': -628462148}

    OBJ = bot(receiver=group_id['receiver'], sender=group_id['sender'])
    OBJ._main_()
    
        






    