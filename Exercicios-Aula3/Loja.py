# 4) Você foi contratado para desenvolver um sistema simples de gerenciamento de
# produtos para uma loja. O objetivo é criar um programa que permita a um usuário
# realizar as seguintes operações em uma lista de produtos:
# 1. Cadastrar Produto: O usuário deve poder inserir o nome e o preço de um novo
# produto. O produto deve ser armazenado em uma lista de dicionários, onde
# cada dicionário representa um produto com suas informações.
# 2. Editar Produto: O usuário deve poder modificar o preço de um produto
# existente. Para isso, o programa deve solicitar o nome do produto que deseja
# editar e, caso ele exista, permitir que o usuário atualize o preço.
# 3. Excluir Produto: O usuário deve ter a opção de remover um produto da lista
# informando o nome do produto a ser excluído.
# 4. Listar Produtos: O programa deve exibir todos os produtos cadastrados,
# mostrando o nome e o preço de cada um.
# 5. Sair: O usuário deve poder sair do sistema a qualquer momento.

produtos = {}

def cadastrar_produto():
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    produtos[nome] = preco
    print(f'Produto {nome} cadastrado com sucesso!')

def editar_produto():
    nome = input('Digite o nome do produto a ser editado: ')
    if nome in produtos:
        novo_preco = float(input('Digite o novo preço: '))
        produtos[nome] = novo_preco
        print(f'Preço do produto {nome} editado com sucesso!')
    else:
        print('Produto não encontrado')
        
def excluir_produto():
    nome = input('Digite o nome do produto a ser excluído: ')
    if nome in produtos:
        del produtos[nome]
        # if produto['nome'] == nome:
            # produtos.remove(produto)
            # print(f'{nome} excluído!')
        print(f'{nome} excluído om sucesso!')
    else:
        print('Produto não encontrado')
        
def listar_produto():
    print('Lista de produtos: ')
    for nome, preco in produtos.items():
        print(f'{nome}: R${preco}')
    
        
while True:
    print('\n1- Cadastrar produto')
    print('2 - Editar produto')
    print('3 - Excluir produto')
    print('4 - Listar produto')
    print('0 - Sair')
    
    opcao = int(input('Digite a opção desejada: '))
    
    match opcao:
        case 1:
            cadastrar_produto()
        case 2:
            editar_produto()
        case 3:
            excluir_produto()
        case 4:
            listar_produto()
        case 0:
            break
        case _:
            print('Digite uma opção válida!')