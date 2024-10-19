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
    def __init__(self, numero, tipo, disponivel=True):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = disponivel
        
    def alterar_disponibilidade (self, disponibilidade):
        self.disponivel = disponibilidade        
    
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.reservas = []
        
    def reservar_quarto(self, quarto):
        if quarto.disponivel:
            self.reservas.append(quarto)
            quarto.alterar_disponibilidade(False)
            print(f'O quarto {quarto.numero} foi reservado para o cliente {self.nome}')
        else:
            print(f'O quarto {quarto.numero} não está disponível!')
            
    def cancelar_reserva(self, quarto):
        if quarto in self.reservas:
            self.reservas.remove(quarto)
            quarto.alterar_disponibilidade(True)
            print(f'A reserva do quarto {quarto.numero} foi cancelada para {self.nome}.')
        else:
            print(f'O quarto {quarto.numero} não está reservado para {self.nome}.')
            
quarto1 = Quarto(14, 'single')
quarto2 = Quarto(15, 'duble')

cliente1 = Cliente('Maria')


cliente1.reservar_quarto(quarto1)
cliente1.reservar_quarto(quarto2)

cliente1.reservar_quarto(quarto1)

cliente1.cancelar_reserva(quarto1)
cliente1.cancelar_reserva(quarto1)

