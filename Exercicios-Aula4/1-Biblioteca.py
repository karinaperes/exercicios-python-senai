# 1. registrar categorias de livros
# 2. cada categoria pode ter vários títulos de livros
# 3. Crie uma função chamada registrar_livros que:
#      aceite uma categoria de livro como primeiro argumento e um número variável de
#      títulos de livros como o restante dos argumentos. 
# A função deve exibir a categoria e listar todos os livros registrados naquela categoria.

def registrar_livros(categoria, *titulos):
    print(f'\nCategoria: {categoria}\n')
    print('Títulos:\n')
    
    for i, livro in enumerate(titulos, 1):
        print(f'{i} {livro}')

registrar_livros('Livros Espíritas', 'Violetas na Janela', 'O Consolador', 'Nosso Lar', 'O Céu e o Inferno\n')
    