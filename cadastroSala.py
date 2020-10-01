class CadastroSala():
    def adicionaVagas(self, sala, vagas):
        sala.vagas += vagas
        sala.disponibilidade = True
