# 1) Fazer um programa que simule uma fila de lotérica. Começar uma lista vazia e dar as
# seguintes opções:
# A) Entrar pessoa (perguntar o nome)
# B) Saiu pessoa (sempre a que entrou primeiro)
# Se a fila acumular 5 pessoas, finalizar o programa e mostrar a ordem da fila

fila = []

acumulado = 0

def entrada():
    pessoa = input('Digite seu nome: ')
    fila.append(pessoa)
    return fila

def saida():
    fila.pop(0)
    return fila

while acumulado < 4:
    acumulado = len(fila)
    print('\nSelecione uma opção:\n')
    print('1 - Entrada')
    print('2 - Saída')
    print('3 - Sair do sistema')
    print('\n--------------------\n')
    opcao = int(input('Opção: '))    
    
    if opcao == 1:
        fila = entrada()
        print('--------------------')
        for i in (fila):
            
            print(fila.index(i) + 1, i)
        print('--------------------')
    
    elif opcao == 2:
        fila = saida()
        print('--------------------')
        for i in (fila):
            
            print(fila.index(i) + 1, i)
        print('--------------------')
    
    elif opcao == 3:        
        for i in (fila):
            print(fila.index(i) + 1, i)
        print('\n~*~*~*~*~*~*~*~*~*~\n')
        print('Sistema finalizado!')
        print('\n~*~*~*~*~*~*~*~*~*~\n')
        break
    
    else:
        print('Escolha uma opção válida')

print('A fila acumulou 5 pessoas!\n')
