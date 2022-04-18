from time import sleep
from functions import *

while True:
    print()
    sleep(1)
    apart('Controlador de Estoque', 46)
    print('''1 - Incluir um Novo produto
2 - Remover um Produto
3 - Listar Todos os Produtos Cadastrados
4 - Listar Informações de um Produto Específico
5 - Editar um Produto
6 - Sair do Programa''')
    print('\033[97;1m=\033[m' * 60)
    choice = select('Digite sua Escolha: ')
    print('')

    if choice == 1:
        apart('Novo Produto', 42)
        name = str(input('Nome do Produto: '))
        value = float(input('Preço do Produto: R$'))
        amount = int(input('Quantidade do Produto: '))
        include(name, value, amount)
        continue

    if choice == 2:
        apart('Remover Produto', 41)
        if len(products) == 0:
            print('\033[31mAinda não foi cadastrado nenhum produto.\033[m')
        else:
            name = str(input('Digite o Nome do Produto Para Remove-lo: '))
            remove(name)
            continue

    if choice == 3:
        apart('Produtos Cadastrados', 107)
        if len(products) == 0:
            print('\033[31mAinda não foi cadastrado nenhum produto.\033[m')
        else:
            list()

    if choice == 4:
        apart('Informações de um Produto Específico', 43)
        name = str(input('Digite o Nome do Produto que Deseja Acessar: ')).strip().title()
        product_list(name)

    if choice == 5:
        apart('Edição de um Produto Específico', 45)
        name = str(input('Digite o Nome do Produto que Deseja Editar: ')).strip().title()
        product_edit(name)

    if choice == 6:
        exit()
        break
