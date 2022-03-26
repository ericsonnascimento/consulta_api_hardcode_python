import requests

def buscar_dados():
    url_all = 'http://127.0.0.1:5000/hoteis'
    r = requests.get(url_all)
    return r.json()

def buscar_dados_id(id):
    url_id = f'http://127.0.0.1:5000/hoteis/{id}'
    r = requests.get(url_id)
    return r.json()

def deletar_id(id):
    requests.delete(f'http://127.0.0.1:5000/hoteis/{id}')

def adicionar_dados(id, nome, cidade, estrelas, diaria):
    payload = dict(nome=f'{nome}', cidade=f'{cidade}', estrelas=f'{estrelas}', diaria=f'{diaria}')
    requests.post(f'http://127.0.0.1:5000/hoteis/{id}', data=payload)

def alterar_dados(id, nome, cidade, estrelas, diaria):
    payload = dict(nome=f'{nome}', cidade=f'{cidade}', estrelas=f'{estrelas}', diaria=f'{diaria}')
    requests.put(f'http://127.0.0.1:5000/hoteis/{id}', data=payload)

menu = ' '

while menu:
    print('''-=-=-=-=-=SOFTWARE DE HOTEIS-=-=-=-=-=-
     [1] Listar todos os hoteis
     [2] Listar pelo ID
     [3] Adicionar hotel
     [4] Alterar hotel
     [5] Excluir hotel
     [6] Sair''')
    menu = int(input('Escolha as opções desejadas: '))

    if menu == 1:
        print(buscar_dados())

    elif menu == 2:
        id = input('Digite o ID do hotel: ')
        print(buscar_dados_id(id=id))

    elif menu == 3:
        id = input('Digite o ID do hotel: ')
        nome = input('Digite o nome do hotel: ').strip().title()
        cidade = input('Digite a cidade do hotel: ').strip().title()
        estrelas = input('Digite as estrelas do hotel: ')
        diaria = input(('Digite o valor da diaria do hotel: '))
        adicionar_dados(id=id, nome=nome, cidade=cidade, estrelas=estrelas, diaria=diaria)
        print('Hotel cadastrado com sucesso!')

    elif menu == 4:
        id = input('Digite o ID do hotel: ')
        nome = input('Digite o nome do hotel: ').strip().title()
        cidade = input('Digite a cidade do hotel: ').strip().title()
        estrelas = input('Digite as estrelas do hotel: ')
        diaria = input(('Digite o valor da diaria do hotel: '))
        alterar_dados(id=id, nome=nome, cidade=cidade, estrelas=estrelas, diaria=diaria)
        print('Hotel cadastrado com sucesso!')

    elif menu == 5:
        id = input('Digite o ID do hotel a ser DELETADO: ')
        deletar_id(id=id)
        print('Hotel deletado com sucesso!')
        '''else:
            print('Hotel não encontrado, tente novamente!')
            id = input('Digite o ID do hotel a ser DELETADO: ')'''

    elif menu == 6:
        break