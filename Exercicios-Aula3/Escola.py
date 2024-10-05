# 5) Você deve criar um CRUD simples para gerenciar uma lista de alunos em uma escola
# utilizando um dicionário em Python. O dicionário será chamado escola, onde a chave
# será o número de matrícula do aluno e o valor será um dicionário contendo o nome, a
# idade e as notas do aluno.
# As funcionalidades do sistema devem incluir:
# 1. Cadastrar um aluno (número de matrícula, nome, idade e notas).
# 2. Editar as informações de um aluno.
# 3. Excluir um aluno.
# 4. Listar todos os alunos.
# 5. Buscar um aluno pelo número de matrícula.
# 6. Calcular a média das notas de um aluno.
# 7. Sair do sistema.

escola = {}

def cadastrar_aluno():
    matricula = input('Número da matrícula: ')
    nome = input('Nome do aluno: ')
    idade = int(input("Idade: "))
    notas = []
    for i in range(3):
        nota = float(input(f'Digite a nota {i + 1}: '))
        notas.append(nota)
    escola[matricula] = {'nome': nome, 'idade': idade, 'notas': notas}
    
def editar_aluno():
    matricula = input('Digite a matrícula do aluno a ser editado: ')
    if matricula in escola:
        nome = input("Digite o novo nome: ")
        idade = int(input('Digite a nova idade'))
        notas = list(map(float, input('Digite as novas notas: ')))
        escola[matricula] = {'nome': nome, 'idade': idade, 'notas': notas}
        print(f'Dados do aluno {nome} editados com sucesso!')
    else:
        print('Aluno não encontrado')
        
def excluir_aluno():
    matricula = input('Digite a matrícula do aluno a ser excluído: ')
    if matricula in escola:
        del escola[matricula]
        print(f'Aluno {matricula} excluído com sucesso!')
    else:
        print('Aluno não encontrado!')
        
def listar_alunos():
  print("Lista de alunos:")
  for matricula, dados in escola.items():
    print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Idade: {dados['idade']}")
        
def buscar_aluno():
  matricula = input("Digite a matrícula do aluno a ser buscado: ")
  if matricula in escola:
    dados = escola[matricula]
    print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Idade: {dados['idade']}")
  else:
    print("Aluno não encontrado")

def calcular_media():
  matricula = input("Digite a matrícula do aluno para calcular a média de notas: ")

  if matricula in escola:
    notas = escola[matricula]["notas"]
    media = sum(notas)/len(notas)
    print(f"A média de notas do aluno {escola[matricula]['nome']} é: {media:.2f}")
  else:
    print("Aluno não encontrado")

while True:
    print('\n1- Cadastrar aluno')
    print('2 - Editar aluno')
    print('3 - Excluir aluno')
    print('4 - Listar alunos')
    print('5 - Buscar aluno')
    print('6 - Calcular média de notas')
    print('0 - Sair')
    
    opcao = int(input('Digite a opção desejada: '))
    
    match opcao:
        case 1:
            cadastrar_aluno()
        case 2:
            editar_aluno()
        case 3:
            excluir_aluno()
        case 4:
            listar_alunos()
        case 5:
            buscar_aluno()
        case 6:
            calcular_media()
        case 0:
            break
        