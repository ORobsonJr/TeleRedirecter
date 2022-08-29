from get_messages import return_messages
from send_message import send_message
from sys import argv 


class __main__:
    def __init__(self) -> None:
        pass

    def install(self): #This function install dependencies
        from os import system

        try:
            system('python3 -m pip install -r tele/requirements.txt') #Install python dependencies
        except Exception as e:
            print('[ERRO]',e)


    def config(self, api_id, api_hash):
        try:
            with open('tele/data.yaml', 'w') as f:
                f.write("API_ID: '{}'\n".format(api_id))
                f.write("API_HASH: "+api_hash) 
                f.close()

        except Exception as error:
            print('[ERRO] Infelizmente occoreu o erro ',error)


if __name__ == '__main__':
    if argv[1] == ('-i' or '--install'): #Install
        __main__().install()

    elif argv[1] == ('-c' or '--config'): #Config data.yaml with id and hash
        __main__().config(
            api_id=input('Digite seu id: '),
            api_hash=input('Digite sua hash: ')
        )

    elif argv[1] =='run':
        exec(open('tele/bot.py').read())

    else:
        space = 4*' '

        print(f"""
        Basic commands to run TeleRedirecter

        -i or --install{space}Install dependencies and modules
        -c or --config{space}Configure api id and hash
        run{space}Run the program 
        """)



    
        


