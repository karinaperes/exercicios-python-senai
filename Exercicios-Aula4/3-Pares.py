#  Crie uma função filtrar_pares que receba uma lista de números. Utilize
# uma função lambda combinada com filter() para filtrar apenas os números pares da
# lista. Retorne a lista filtrada com os números pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 20]
filtrar_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(filtrar_pares)
