## Instruções de execução da API.

Aplicação desenvolvida com Django RestFramework.


1- docker-compose up --build ->(Constroi as imagens do postgresql bem como a api)

1.2- Caso necessário execute o comando "python3 manage.py makemigrations djapi", para a migrar a tabela.

2- docker-compose up -d ->(esse comando executa os containers mas não mostra os logs.)

3- docker-compose down ->(para derrubar os containers)

4- docker stop + nome do container ou seu id para parar os container.

## Observações de uso:
Após os containers e aplicação estarem em execução, no navegador de sua escolha busque pelo endereço, 
localhost:8000/parking; na api do DRF pode-se fazer um post no campo de("plate-number"), exemplo KLM-5050 para adicionar placas e ver os respectivos respostas JSON.

É possivel deletar colocando na URL /parkin/ + numero do ID.

A aplicação ira restringir se não usar os padrões de letras maísculas assim como o uso do ífem, será dado um alerta.

Também é possível fazer buscas por filtro.
