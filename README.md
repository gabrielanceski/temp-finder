# Temp Finder

Este script foi desenvolvido com o intuito de encontrar um site específico numa lista de urls temporárias que não possuem um domínio fixo. Para que isso aconteça, o script faz uma requisição para cada url da lista e verifica se o site que está sendo procurado está presente no corpo da resposta. Caso esteja, o script retorna a url que contém o site procurado.

## Como usar

- Preencha o arquivo urls.txt com as urls que deseja verificar
- Execute o script com o comando `python temp_finder.py`
- Digite o site que deseja encontrar
- Aguarde o script terminar de executar
- O script irá retornar a url que contém o site procurado ou uma mensagem de erro caso não encontre
