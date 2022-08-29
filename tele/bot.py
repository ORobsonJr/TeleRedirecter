from get_messages import return_messages
from send_message import send_message
from yaml import load
from yaml.loader import SafeLoader

class auth:
    with open('tele/data.yaml', 'r') as f:
        data = load(f, Loader=SafeLoader)
        
        api_id = data['API_ID']
        api_hash = data['API_HASH']

class bot:
    def __init__(self, receiver, sender):
        self.api_id = auth.api_id
        self.api_hash = auth.api_hash
        
        self.receiver = receiver
        self.sender = sender

    def _main_(self):
        while True:            
            last_message = [] #Store the last message received
            value = 0
            receive = return_messages(api_id=self.api_id, api_hash=self.api_hash)
            send_ = send_message(api_id=self.api_id, api_hash=self.api_hash)


            while True:
                message = receive.get_all(group_link=self.sender) #Get the message 
                try:
                    last_message.index(message) #This is used to avoid loop problems
                    value = 1

                except ValueError:
                     last_message.append(message)
                     value = 0
                     
                if message != None:
                    if value == 0:
                        print('Menssagem recebida: ', message)
                        send_.send_to(message=message, group_link=self.receiver)



            

if __name__ == '__main__':
    try:
        bot(receiver=input('Digite o link do grupo que vai receber menssagens: '),
            sender=input('Digite o link do grupo que vai enviar menssagens: '))._main_()
    
    except ValueError:
        print('Por favor execute "python3 tele -c" primeiro')


    






    