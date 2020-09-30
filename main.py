from datetime import datetime
from model.usuario import User
from model.sala import Sala
from model.reserva import Reserva
from cadastroUsuario import CadastroUsuario
from cadastroSala import CadastroSala
from cadastroReserva import CadastroReserva

lista = []

sala01 = Sala(1)

lista.append(vars(sala01))

print(lista)

cad = CadastroSala()
cad.adicionaVagas(sala01, 10)

print(vars(sala01))

reserva01 = Reserva(1,sala01,datetime.today().strftime('%Y-%m-%d'))

cadReserva = CadastroReserva()
cadReserva.reservarSala(reserva01.sala)

print(vars(reserva01))
print(vars(sala01))





# pessoa = User(10,'João', '1191492-3231')
# pessoa2 = User(11,'Pedro', '1191492-3231')

# cadastro = CadastroUsuario()
# cadastro.add(pessoa, lista)
# cadastro.add(pessoa2, lista)

# if(len(lista) == 2):
#     print('Passou')


# print(lista)
