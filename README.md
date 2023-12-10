# Biciletario-Inteligente
Trabalho de Tópicos em IOT
INSTRUÇÕES:

1- Clonar o repositório;
2- No postman, clicar no botão "import"(canto superior esquerdo) e arrastar o Bicicletario.postman_collection.json para a área designada;
3- Agora, abra o repositório no terminal e digite "code .", ao fazer isso abrirá todo o código no VS code;
4- Para colocar pra funcionar, no terminal do repositório digite "docker compose up -d" e o sistema irá inicializar no Docker;
5- No postman, serápossível ver 4 métodos, sendo 2 POSTS, 1 GET e 1 PATCH. Primeiro, será necessário criar o serviço, então clique no primeiro GET. Acessando o seu body é possivel ver o apikey, o broker, o tipo de entidade e o resource. Clique
em "send" no canto superior direito para iniciar a aplicação;
6- No segundo "POST", provisionaremos a bicicleta, chamada de bike001, abrindo o seu body é possível ver seu nome de entidade, seu tipo, o tipo de transporte, os comandos, e o tipo estático, que no caso eu coloquei o modelo da bicicleta.
Aperte em "send" para criar a bicicleta;
7- Agora, em "GET", se clicar em "send", verá que somente aparece o id da bicicleta e os comandos acompanhados de "";
8- Vá para o "PATCH", vai ver que vai estar o comando "start" e abaixo o tipo e o valor, aperte em "send" e ele iniciará o envio de dados;
9- Abrindo novamente o "GET", verá que agora também é possível vizualizar o modelo da bicicleta, o horário(infelizmente está no UTC, não consegui corrigir isso), a localização(que poderá apresentar ou "in" ou "out"), o start_info e o
start_status;
10- Agora com que há o envio de dados, apertando o "send" na página do GET a cada 5 segundos, verá que o horário atualiza e tambéeeeem há a chance da localização ter mudado de "in" para "out" ou de "out" para "in, indicando que a bicicleta 
está saindo ou entrando do bicicletário respectivamente;


O CÓDIGO:

1- No docker-compose.yml estão separados todos os componentes do sistema, o Orion(context broker), o IOT-agent, o Mongo-db, e o Dummy device(responsável por gerar os dados para o IOT-agent). Todos estão comentados no código.
2- Dentro da pasta do Dummy-device há o dockerfile, usado para criar e configurar o contêiner para o provedor de contexto, o requirements.txt, usado para carregar bibliotecas python no contêiner e o app.py, usado para servir o aplicativo
Flask para criar um dispositivo fictício capaz de enviar medições aleatórias e receber comandos;
