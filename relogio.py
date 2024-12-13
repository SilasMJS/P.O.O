class Relogio_digital_simples:
    def __init__(self, hora, minuto) -> None:
        self.hora = hora
        self.minuto = minuto
    
    def ajustar_horario(self, nova_hora, novo_minuto):
        if 0 <= nova_hora < 24 and 0 <= novo_minuto < 60:
            self.hora = nova_hora
            self.minuto = novo_minuto
            return f'Hora Ajustada para {self.hora:02}:{self.minuto:02}'
        else:
            raise Exception("Erro: Hora ou minutos inválidos.")
        
    def exibir_horario(self):
        return f'Horário Atual: {self.hora:02}:{self.minuto:02}'
        
horario = Relogio_digital_simples(23,58)
print(horario.ajustar_horario(13,37))
print(horario.exibir_horario())
