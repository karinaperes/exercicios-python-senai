# 3) 
# 1. Adicionar Produtos à lista de produtos com nome, preço e quantidade em estoque
# 2. Registrar Venda diminuindo a quantidade de um produto no estoque e adicionando a venda a uma lista de vendas
# 3. Exibir Produtos Disponíveis com quantidade em estoque
# 4. Exibir Vendas Realizadas o produto vendido, a quantidade e o valor total da venda
# 5. Calcular Receita Total gerada pelas vendas realizadas
# 6. Identificar Produto Mais Vendido, que gerou o maior valor em vendas
# 7. Reabastecer Estoque de produtos no estoque

lista_produtos = []
vendas = []

def cadastrar_produto():
    nome = input('\nDigite o nome do produto \n').capitalize()
    preco = float(input('\nDigite o valor do produto \n'))
    estoque = int(input('\nDigite a quantidade do produto em estoque \n'))
    
    lista_produtos.append({'nome': nome, 'preco': preco, 'estoque': estoque})
    
    print(f'\n{nome} cadastrado com sucesso!')
    print(lista_produtos)
    
def vender_produto():
    nome = input('\nDigite o nome do produto\n').capitalize()
    quantidade = int(input('\nDigite a quantidade vendida:\n'))
    
    for i in lista_produtos:
        if i['nome'] == nome:
            if i['estoque'] >= quantidade:
                i['estoque'] -= quantidade                
                vendas.append({'produto': nome, 'quantidade': quantidade, 'valor': i['preco']*quantidade})
                print(f'Venda efetuada:\n {quantidade} {nome}')
            else:
                print('Quantidade insuficiente no estoque')
            break
    else:
        print('Produto não encontrado')   
    
def listar_produtos():
    print('Produtos em estoque:')
    print('--------------------------')
    for produto in lista_produtos:
        if produto['estoque'] > 0:
            print(f"{produto['nome']} - Quant: {produto['estoque']} - R${produto['preco']:.2f} ")    
    print('--------------------------')
def vendas_realizadas():
    print('Produtos vendidos:\n')
    print('--------------------------')
    for venda in vendas:
        print(f"{venda['produto']} - {venda['quantidade']} - {venda['valor']}")
    print('--------------------------')
        
def calcular_receita_total():
  receita_total = sum(venda['valor'] for venda in vendas)
  print('**********************')
  print(f"Receita total: {receita_total}")
  print('**********************')
        
def identificar_produto_mais_vendido():
    vendas_por_produto = {}
    for venda in vendas:
        if venda['produto'] in vendas_por_produto:
            vendas_por_produto[venda['produto']] += venda['valor']
        else:
            vendas_por_produto[venda['produto']] = venda['valor']
    produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)
    print(f'Produto mais vendido: {produto_mais_vendido}')  
    
def reabastecer_estoque():
  nome = input("Digite o nome do produto: ")
  quantidade = int(input("Digite a quantidade a ser reabastecida: "))

  for produto in lista_produtos:
    if produto["nome"] == nome:
      produto["quantidade"] += quantidade
      print(f"Estoque de {nome} reabastecido com sucesso!")
      break
    else:
      print("Produto não encontrado.")
                    
while True:
    print('\nEscolha uma opção:\n')
    print('1 - Cadastrar')
    print('2 - Vender')
    print('3 - Listar')
    print('4 - Vendas')
    print('5 - Receita Total')
    print('6 - Produto mais vendido')
    print('7 - Reabastecer Estoque')
    print('0 - Sair')
    
    opcao = int(input('\nEscolha uma opção: '))
    
    match opcao:
        case 1:
            cadastrar_produto()
        case 2:
            vender_produto()
        case 3:
            listar_produtos()
        case 4:
            vendas_realizadas()
        case 5:
            calcular_receita_total()
        case 6:
            identificar_produto_mais_vendido()
        case 7:
            reabastecer_estoque()
        case 0:
            break
        case _:
            print('Opção inválida!')
        