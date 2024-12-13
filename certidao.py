from datetime import date
from datetime import time

class Certidao:
    def __init__(self, nome, sexo, nome_mae, cidade, estado, data_nasc, hora_nasc = "Não Informado", nome_pai = "Não Informado") -> None:
        self.nome = nome
        self.sexo = sexo
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai
        self.cidade = cidade
        self.estado = estado
        self.data_nasc = self.valida_data(data_nasc)
        self.hora_nasc = hora_nasc if hora_nasc in ("Não Informado") else self.valida_hora(hora_nasc)
        
    def valida_data(self,data):
        try:
            data = f"{data[6:]}-{data[3:5]}-{data[:2]}"
            data = date.fromisoformat(data)
            data = data.strftime("%d/%m/%Y")
            return data
        except:
            raise ValueError("Erro: Data Inválida!")
            
    def valida_hora(self, horario):
        try:
            horario = time.fromisoformat(horario)
            horario = horario.isoformat('minutes')
            if horario >= "12":
                return horario + "PM"
            return horario + "AM"
        except:
            raise ValueError("Erro: Horario Inválido!")
    
    def __str__(self) -> str:
        certidao = f"""\n**************Certidão de Nascimento*****************
        Nome: {self.nome}
        Sexo: {self.sexo}
        Nome da Mãe: {self.nome_mae}
        Nome do Pai: {self.nome_pai}
        Data do Nascimento: {self.data_nasc}
        Hora do Nascimento: {self.hora_nasc}
        Cidade: {self.cidade}
        Estado: {self.estado}
*****************************************************\n"""
        return certidao

def main():
    cert = Certidao("Silas Malaquias de Jesus Silva", "Masculino", "Francisca", "Água Branca", "Piauí", "06/07/2000","11:40")
    print(cert)
    cert2 = Certidao("Salatiel", "Masculino","Francisca","Água Branca","Piauí","09/03/2002", nome_pai="Francisco")
    print(cert2)
    #         0123456789
    # data = "06-07-2000"
    # data = f"{data[6:]}-{data[3:5]}-{data[:2]}"
    # print(data)
    
if __name__ == "__main__":
    main()