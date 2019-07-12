# Rafinhas Lava-Jato

## Como executar em seu compultador?
Muito simples, apenas digite "sudo docker-compose up --build", não precisa de sudo se você não estiver no linux. Após fazer o build, você pode iniciar a aplicação apenas usando "sudo docker-compose up". Para encerrar a aplicação, basta dar um "ctrl+c"!

Sempre que houver alterações no Dockerfile ou no docker-compose, deve ser dado um --build, para que a alteração seja feita com sucesso.

## Problemas Solucionados
1. Intalando Psycopg2 em docker image: Este [link](https://stackoverflow.com/questions/46711990/error-pg-config-executable-not-found-when-installing-psycopg2-on-alpine-in-dock) explica como solucionar esse problema dentro do docker.
2. ...