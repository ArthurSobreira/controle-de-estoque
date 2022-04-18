products = list()


def apart(txt, col):
    size = 60
    print('\033[97;1m=\033[m' * size)
    print(f'\033[{col};1m{txt:^{size}}\033[m')
    print('\033[97;1m=\033[m' * size)


def select(txt):
    while True:
        try:
            choice = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro, dado inválido, tente novamente!\033[m')
            continue
        else:
            if choice in range(1, 7):
                break
            else:
                print('\033[31mErro, dado inválido, tente novamente!\033[m')
    return choice


def include(name, value, amount):
    products.append({'name': name.strip().title(), 'value': value, 'amount': amount})
    print(f'\033[32mProduto {name} Cadastrado com Sucesso!!\033[m')


def remove(name):
    tot = 0
    for c in products:
        if c['name'] == name:
            tot += 1
            products.remove(c)
            print(f'\033[32mProduto {name} Removido Com Sucesso!!\033[m')
            break
    if tot == 0:
        print(f'\033[31mO Produto {name} não foi cadastrado, tente novamente!\033[m')


def list():
    print('   Nome', ' ' * 17, 'Valor', ' ' * 14, 'Quantidade')
    print('\033[97;1m=\033[m' * 60)
    for c in products:
        print(f' > {c["name"]:<20}', end='')
        print(f'> R$ {c["value"]:<15.2f} ', end='')
        print(f'> {c["amount"]} Unidades')
    print('\033[97;1m=\033[m' * 60)


def product_list(name):
    tot = 0
    for c in products:
        if c['name'] == name:
            tot += 1
            print(f'Nome do Produto: {c["name"]}')
            print(f'Valor por Unidade: R${c["value"]:.2f}')
            print(f'Total de Unidades: {c["amount"]}')
            print(f'Preço do Lote: R${(c["amount"]) * (c["value"]):.2f}')

    if tot == 0:
        print(f'\033[31mO Produto {name} não foi cadastrado, tente novamente!\033[m')


def product_edit(name):
    tot = 0
    for c in products:
        if c['name'] == name:
            tot += 1
            products.remove(c)
            v = float(input('Preço do Produto: R$'))
            a = int(input('Quantidade do Produto: '))
            include(name, v, a)
            break
    if tot == 0:
        print(f'\033[31mO Produto {name} não foi cadastrado, tente novamente!\033[m')


def exit():
    apart('Fim do Programa, Volte Sempre!!', 31)
