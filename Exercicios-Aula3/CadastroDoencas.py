# 2) Desenvolver um programa que peça ao usuário o número de doenças a cadastrar,
# no qual ele deve cadastrar o nome da doença e se ela é transmitida por vírus, bactéria
# ou por ambos. Ao final, mostrar quatro listas: doenças transmitidas por vírus, doenças
# transmitidas por bactérias, doenças transmitidas por ambos, lista com todas doenças.

doencas = {}

def cadastro_doenca():
    doenca = input('Nome da doença: ')
    transmissao_virus = input('Transmitida por vírus? Digite: \n 1 - Sim \n 2 - Não?\n')
    transmissão_bacteria = input('Transmitida por bactéria? Sim ou Não?\n')

    doencas[doenca] = {
        'transmissao_virus': transmissao_virus == '1',
        'transmissao_bacteria': transmissão_bacteria == '1' }
    
    print(f'Doença {doenca} cadastrada com sucesso!\n')
    print(doencas)
    
    return doencas

def listar_doencas():
    lista_virus = []
    lista_bacteria = []
    lista_ambos = []
    lista_todas = []
    
    for doenca, info in doencas.items():
        if info['transmissao_virus'] and info['transmissao_bacteria']:
            lista_ambos.append(doenca)
        elif info['transmissao_virus']:
            lista_virus.append(doenca)
        elif info['transmissao_bacteria']:
            lista_bacteria.append(doenca)        
            
        lista_todas.append(doenca)
        
    print('\n Doenças transmitidas por vírus: ', lista_virus)
    print('\n Doenças transmitidas por bactéria: ', lista_bacteria)
    print('\n Doenças transmitidas por ambos: ', lista_ambos)
    print('\n Todas as doenças cadastradas: ', lista_todas)
    
num_cadastro = int(input('Quantos cadastros deseja efetuar?:\n'))

while len(doencas) < num_cadastro:
    cadastro_doenca()
    
listar_doencas()
        