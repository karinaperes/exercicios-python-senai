# Você trabalha em uma loja online e precisa ordenar os produtos por preço. Crie uma
# lista de produtos onde cada produto é representado como uma tupla com o nome e o
# preço. Use a função sorted() combinada com uma função lambda para ordenar essa
# lista de acordo com o preço de cada produto.

produtos = []

while True:
    nome = input('Digite o nome do produto: ')
    if nome == 'sair':
        break
    else:
        preco = float(input('Digite o preço do produto: '))
        produtos.append(nome, preco)

lista_ordenada = sorted(produtos, key=lambda produto: produto[1])
for produto in lista_ordenada:
    print(f'{produto[0]}: R${produto[1]}')
    

