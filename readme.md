# Rafinhas Lava-Jato

## Sumário
1. [Sumário](#Sumário)
2. [Motivação](#Motivação)
3. [Como executar em seu compultador?](#Como-executar-em-seu-compultador)
4. [Estudos Importantes](#Estudos-Importantes)
5. [Problemas Solucionados](#problemas-solucionados)

## Motivação
O Projeto Rafinhas foi um projeto que a empresa Dual Junior fechou com uma empresa de lava-jato e estacionamento. Seu principal problema era gerenciar tudo usando papeis e a cabeça. Foi proposto uma mudança de rumo, a aquisição de uma aplicação que pudesse fazer todo o trabalho. De início ela foi feita em Java, mas dai migramos para o Python e o Conceito de API e RestFramework.

## Como executar em seu compultador?
Muito simples, como nossa aplicação está usando docker, você não precisa se preocupar com nada, apenas seguir o passo a passo abaixo:
### Primeira Vez
1. Clone a aplicação para o seu pc
2. Na pasta raiz execute o comando "docker-compose up -d --build"
3. Execute o comando "docker-compose run --rm app migrate
4. Sua aplicação está pronta e operando normalmente

### Outras vezes
Apenas execute "docker-compose up -d" e pronto, sua aplicação estará rodando normalmente. Em qualquer dos casos execute "docker-compose down" para derrubar a aplicação. Veja [Problemas Solucionados](#problemas-solucionados) para maiores duvidas.

### Para rodar tesdocker tag local-image:tagname new-repo:tagnametes???
Sim, da sim, inclusive já existe um sob medida, basta executar "docker-compose run --rm app test rafinhas.tests.Fluxo"

IMPORTANTE: Sempre que houver alterações no Dockerfile ou no docker-compose, deve ser dado um --build, para que a alteração seja feita com sucesso.

## Estudos Importantes
- Como funciona o Django Database? Na [documentação](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) explica sobre como usar o Django Models. Vale a pena ler antes de usar a aplicação.

## Problemas Solucionados
1. Intalando Psycopg2 em docker image: Este [link](https://stackoverflow.com/questions/46711990/error-pg-config-executable-not-found-when-installing-psycopg2-on-alpine-in-dock) explica como solucionar esse problema dentro do docker.
2. Importante também ficar de olho em todas as pastas, se elas estão mapeadas pros locais certos. Como nesta aplicação está se usando o alpine, alguns comandos são diferentes, por exemplo, não existe apt-get, mas sim apk. O bin/bash fica bin/sh.
3. Muitas vezes o linux não vai aceitar o comando docker-compose (se já tiver sido instalado), para resolver o problema, segue o [link](https://docs.docker.com/install/linux/linux-postinstall/) aonde tem o passo a passo para resolver este problema.
4. ...
