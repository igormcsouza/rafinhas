# Rafinhas Lava-Jato

## Como executar em seu compultador?
Muito simples, apenas digite "sudo docker-compose up --build", não precisa de sudo se você não estiver no linux. Após fazer o build, você pode iniciar a aplicação apenas usando "sudo docker-compose up". Para encerrar a aplicação, basta dar um "ctrl+c"!

Sempre que houver alterações no Dockerfile ou no docker-compose, deve ser dado um --build, para que a alteração seja feita com sucesso.

## Estudos Importantes
- Como funciona o Django Database? Na [documentação](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) explica sobre como usar o Django Models. Vale a pena ler antes de usar a aplicação.

## Problemas Solucionados
1. Intalando Psycopg2 em docker image: Este [link](https://stackoverflow.com/questions/46711990/error-pg-config-executable-not-found-when-installing-psycopg2-on-alpine-in-dock) explica como solucionar esse problema dentro do docker.
2. Importante também ficar de olho em todas as pastas, se elas estão mapeadas pros locais certos. Como nesta aplicação está se usando o alpine, alguns comandos são diferentes, por exemplo, não existe apt-get, mas sim apk. O bin/bash fica bin/sh.
3. 
