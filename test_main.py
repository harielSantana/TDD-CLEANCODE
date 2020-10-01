import unittest
from datetime import datetime

from model.usuario import User
from model.reserva import Reserva
from model.sala import Sala
from cadastroReserva import CadastroReserva
from cadastroSala import CadastroSala
from cadastroUsuario import CadastroUsuario

class Test(unittest.TestCase):
    
    def test_cadastro_um_usuario(self):
        newList = []
        newUser = User(1,'Ruan', '(11)91111-1111')
        register_new_user = CadastroUsuario()
        register_new_user.add(newUser, newList)
        self.assertEqual(len(newList),1,f"Should return 1 instead of {len(newList)} users in a list")

    def test_reserva_usuario(self):
        sala1 = Sala(1)
        usuario = User(1,"Igor","11952762619")
        reserva = Reserva(usuario,sala1,datetime.today().strftime('%Y-%m-%d'))
        lista_sala_reservada = [reserva]

        cad_sala = CadastroSala()
        cad_sala.adicionaVagas(sala1,1)

        cad_reserva = CadastroReserva()
        retorno = cad_reserva.verifica_duplicidade(reserva,lista_sala_reservada)
        self.assertTrue(retorno,"Should return True when a booking already exists in a list of book")
    
    # def test_reserva_usuario(self):
    #     sala1 = Sala(1)
    #     sala2 = Sala(2)
    #     usuario = User(1,"Igor","11952762619")
    #     usuario1 = User(2,"Hariel","11952762619")
    #     reserva = Reserva(usuario,sala1,datetime.today().strftime('%Y-%m-%d'))
    #     reserva1 = Reserva(usuario1,sala1,datetime.today().strftime('%Y-%m-%d'))
        
    #     lista_sala_reservada = []

    #     cad_sala = CadastroSala()
    #     cad_sala.adicionaVagas(sala1,1)
    #     cad_sala.adicionaVagas(sala2,1)

    #     cad_reserva = CadastroReserva()
    #     if  not cad_reserva.verifica_duplicidade(reserva,lista_sala_reservada):
    #         cad_reserva.reservarSala(sala1)
    #         print(vars(sala1))
        
    #     if  not cad_reserva.verifica_duplicidade(reserva1,lista_sala_reservada):
    #         print(cad_reserva.reservarSala(sala1))
    

if __name__ == '__main__':
    unittest.main()
    