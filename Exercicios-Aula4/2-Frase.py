
# 1. criar função processar_frase que:
# • Receba uma string de frase.
# • Divida essa frase em palavras usando split().
# • Concatene as palavras de volta, mas desta vez separadas por um caractere
# especial de sua escolha (por exemplo, #).
# • Exiba tanto a lista de palavras quanto a frase concatenada com o novo
# separador.

def processar_frase(frase, separador):
    palavras = frase.split()
    print('Lista palavras', palavras)
    
    nova_frase = separador.join(palavras)
    print('Frase concatenada: ', nova_frase)
    
processar_frase('Python é uma linguagem de programação', ".")
    