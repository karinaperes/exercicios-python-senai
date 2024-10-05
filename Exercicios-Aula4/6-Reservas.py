# Você está desenvolvendo um sistema para gerenciar reservas em um hotel. O
# sistema deve permitir que um cliente faça reservas de quartos e que o hotel
# acompanhe a disponibilidade dos quartos. 
# Cada quarto deve ter um número, 
# um tipo (single, double, suite) 
# e um status que indique se está disponível ou não. 
# Cada cliente deve ter um nome e uma lista de reservas.
# 1. Crie uma classe Quarto que tenha os atributos:
# numero, 
# tipo e 
# disponivel (booleano).
# 2. Crie uma classe Cliente que tenha os atributos:
# nome e 
# reservas (lista de objetos da classe Quarto).
# 3. Adicione um método na classe Cliente para:
# reservar um quarto e outro para
# cancelar uma reserva.
# 4. Adicione um método na classe Quarto para mudar o status de disponivel.


class Quarto:
    def __init__(self, numero, tipo, disponivel):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = disponivel
    
class Cliente:
    def __init__(self, )