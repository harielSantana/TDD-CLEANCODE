class CadastroReserva():
    def reservarSala(self, sala):
        if sala.vagas >= 1 and sala.disponibilidade == True:
            sala.vagas -= 1 
        else:
            return f"Sala {sala.numero} não tem vagas"

    def verifica_duplicidade(self,reserva,lista_reserva):
        for res in lista_reserva:
            if reserva.usuario.id == res.usuario.id and reserva.date == res.date:
                return True
            else:
                return False
            
    