# soma dos comprimentos de várias palavras
# Crie uma função chamada somar_comprimentos que
# aceite um número variável de palavras utilizando *args e calcule o comprimento total
# dessas palavras.

def somar_comprimentos(*palavras):
    comprimento_total = sum(len(palavra) for palavra in palavras)
      
    print(comprimento_total)

somar_comprimentos('aula', 'garrafa', 'mouse')
