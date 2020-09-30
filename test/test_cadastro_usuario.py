import unittest
from model.usuario import User
from cadastroUsuario import CadastroUsuario

class NewTest(unittest.TestCase):
    
    def test_cadastro1(self):
        pessoa = User(10,'João', '1191492-3231')
        lista = []
        if(len(lista) == 1):
            self.assertEqual()

    def test_cadastro2(self):
        pass


if __name__ == '__main__':
    unittest.main()
    