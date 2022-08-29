<h1>TeleRedirecter</h1>

### Tópicos
* [Descrição do projeto](#descrição-do-projeto)
* [Como funciona o TeleRedicter](#como-funciona-o-teleredirecter)
* [Como instalar](#como-instalar-e-configurar)
* [Como Usar o TeleRedirecter](#como-usar)

## Descrição do projeto
<p>O Teleredirecter é um software construído em Python que recebe menssagens de um grupo e encaminha para outro grupo</p>

## Como funciona o TeleRedirecter
<h4>Funcionalidade</h4>
<p>O TeleRedirecter funciona através de um loop em modo escuta no grupo enviador - grupo que vai receber as menssagens e assim que recebe alguma menssagem, envia para o grupo alvo - grupo que recebe as menssagens.

O sistema usa um arquivo dabatase como forma de armazenar a SessionId do telegram - para saber mais clique <a href="https://docs.telethon.dev/en/stable/concepts/sessions.html">aqui</a>; assim não precisando autenticar toda vez que for executar o programa.
</P>

<h4>Tecnologias usadas para o projeto</h4>
<ul>
<li>Git & GitHub</li>
<li>Telethon</li>
<li>Python3</li>
</ul>

## Como instalar e configurar
Na pasta do projeto "TeleRedirecter" digite algo como: 
:heavy_check_mark: 'python3 tele -i':


<h5>Solução para possível erro na instalação do yaml</h5>
<img src="https://user-images.githubusercontent.com/109431368/187282657-9f8a943e-d717-4cbf-81fc-0d32a4d80644.png"/>


:heavy_check_mark: `$ sudo apt-get install python-yaml`:
:heavy_check_mark: `$ sudo yum install python-yaml`:

<h3>Como configurar</h3>
<p> Aqui iremos configurar as chave api que você pode encontrar mais aqui <a href="https://my.telegram.org/">aqui</a>;, você pode configurar através do arquivo data.yaml que se encontra na pasta tele ou pode configurar pelo comando :heavy-check_mark: 'python tele -c': do qual irá pedir seu id e hash.</p>

## Como usar
<p>O uso do projeto é bem simples basta digitar :heavy-check_mark: 'python3 tele run': e caso você tenha seguido os procedimentos acima </p>

<span class="bolded">Obs.: Para ajuda apenas digite -h ou --help como argumento</span>





