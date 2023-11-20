import requests
import re

LINE_LENGTH = 64

searchName = input('Informe o site que deseja encontrar: ')

urlFile = open('urls.txt', 'r')
urls = urlFile.readlines()
urlFile.close()

print('Buscando por: ' + searchName)

for url in urls:
    url = url.strip()
    if not (url.startswith('https://') and url.startswith('http://')):
        url = 'http://' + url

    try:
        response = requests.get(url)
    except:
        print('Não foi possível acessar o site: ' + url)
        continue

    content = response.text
    foundPattern = re.search(r'<title>(.*?)</title>', content)

    if foundPattern:
        group = foundPattern.group(1)
        print(url + ' -> ' + group)
        if group.lower().find(searchName.lower()) != -1:
            print('-' * LINE_LENGTH)
            print('Termo de busca encontrado na url "' + url + '":')
            print(url + ' -> ' + group)
            print('-' * LINE_LENGTH)
            exit()
            
print('-' * LINE_LENGTH)
print('Nenhum termo de busca com o nome "' + searchName + '" foi encontrado.')
print('-' * LINE_LENGTH)
