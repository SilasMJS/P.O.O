from datetime import date
from datetime import datetime
class Veiculo:
    def __init__(self, chassi, marca, modelo, ano, placa = "Não Possui", cor = "Não Especificada", proprietario = "Não Especificado", quilometragem = 0) -> None:
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = self.valida_Ano(ano)
        self.placa = placa
        self.cor = cor 
        self.proprietario = proprietario
        self.quilometragem = quilometragem

    def valida_Ano(self, ano):
        try:
            datetime.strptime(str(ano), "%Y")
            if 1800 <= ano <= int(date.strftime(date.today(),"%Y")):
                return ano
            else:
                raise ValueError("Ano Inválido!")
        except ValueError:
            raise ValueError("Ano Inválido!")


    def __str__(self) -> str:
        saida = f"""
************Especificações do Veículo************
    Chassi: {self.chassi}
    Marca: {self.marca}
    Modelo: {self.modelo}
    Ano: {self.ano}
    Placa: {self.placa}
    Cor: {self.cor}
    Proprietario: {self.proprietario}
    Quilometragem: {self.quilometragem} Km
************************************************"""
        return saida

def main():
    veiculo1 = Veiculo("20jh4", "Aleatorio", "Modelo_A", 2023, "AIX-2341", "Azul")
    print(veiculo1)
    veiculo2 = Veiculo("20jh4", "Aleatorio", "Modelo_A", 1899, "AIX-2341", "Azul", quilometragem=10000)
    print(veiculo2)
if __name__ == "__main__":
    main()