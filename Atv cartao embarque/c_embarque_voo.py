# Utilizando o processo de abstração, implemente uma classe em Python que represente um
# cartão de embarque de voo. Identifique atributos mutáveis e imutáveis, implemente um
# construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as
# validações possíveis. Crie objetos para testar os métodos implementados.

# Especificações:
# 1. Atributos imutáveis:
# o Nome do passageiro
# o Número do voo
# o Código da reserva (localizador)
# o Data e hora do embarque (utilizar biblioteca datetime para validação)

# 2. Atributos mutáveis:
# o Status do check-in (realizado ou não)
# o Assento

# 3. Métodos sugeridos:
# o Um método para realizar o check-in, que altera o status e associa um assento
# (aleatório) disponível ao passageiro.
# o Um método para alterar o assento (apenas se o check-in já tiver sido
# realizado).
# o Validações para garantir que assentos indisponíveis não sejam atribuídos e
# que o check-in só possa ser feito uma vez.

# 4. Requisitos de validação:
# o O código da reserva deve ter 6 caracteres alfanuméricos.
# o A hora do embarque não pode ser retroativa em relação ao momento de
# execução do código.

# 5. Teste:
# o Crie pelo menos três objetos da classe, representando cartões de embarque
# diferentes.
# o Demonstre os métodos implementados e suas validações em ação.

from datetime import datetime
import random
import string
class Cartao_Embarque_voo:
    def __init__(self, nome, num_voo, cod_reserva, data_embarque, hora_embarque) -> None:
        
        # Atributos Imutáveis
        self.__nome = nome
        self.__num_voo = num_voo
        self.__cod_reserva = self.valida_cod_reserva(cod_reserva)
        self.__data_embarque = self.valida_data(data_embarque)
        self.__hora_embarque = self.valida_hora(hora_embarque)
        
        # Atributos Mutáveis
        self.__checkin = "Não Realizado"
        self.__assento = "Nenhum"
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def num_voo(self):
        return self.__num_voo
    
    @property
    def cod_reserva(self):
        return self.__cod_reserva
    
    @property
    def data_embarque(self):
        return self.__data_embarque
    
    @property
    def hora_embarque(self):
        return self.__hora_embarque
    
    @property
    def assento(self):
        return self.__assento
    
    @property
    def checkin(self):
        return self.__checkin
    
    # Validando Reserva
    def valida_cod_reserva(self, reserva):
        if len(reserva) != 6 and not reserva.isalnum():
            raise ValueError("Código Inválido!")
        # verificando se contem letra
        contem_letra = any(char.isalpha() for char in reserva)
        # verificando se contem numero
        contem_numero = any(char.isdigit() for char in reserva)
        if contem_letra and contem_numero:
            return reserva
        else:
            raise ValueError("Código Inválido!")
    
    # Validando data 
    def valida_data(self, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data Inválida!")
        
    # Validando hora, a validação da hora permite que a hora seja retroativa com a condição que o dia seja o seguinte ao da maquina
    # caso contrario exibira um erro de retroatividade na hora
    def valida_hora(self, hora):
        try:
            hora = datetime.strptime(hora, "%H:%M").time()
            hora_atual = datetime.now().time()
            if self.__data_embarque.date() >= datetime.today().date():
                if self.__data_embarque.date() == datetime.today().date() and hora <= hora_atual:
                    raise ValueError("Hora Inválida! Hora Retroativa!")
                return hora
            else:
                raise ValueError("Data e Hora Retroativa!")
        except ValueError:
            raise ValueError("Hora Inválida!")
        
    # Realizando Check-in
    def check_in(self, assentos_disponiveis):
        if(self.__checkin == "Não Realizado"):
            self.__checkin = "Realizado!"
            self.__assento = random.choice(assentos_disponiveis)
            assentos_disponiveis.remove(self.assento)
        else:
            raise ValueError("Check-in Ja Realizado!")
    # Mudando Assendo caso o chack-in esteja realizado
    def mudar_assento(self, novo_assento, assentos_disponiveis):
        if(self.__checkin == "Não Realizado"):
            raise ValueError("O Check-in Não Realizado!")
        if (novo_assento not in assentos_disponiveis):
            raise ValueError("Assento solicitado não esta disponivel!")
        if(novo_assento == self.__assento):
            raise ValueError("Assento solicitado é igual ao seu Assento atual!")
        else:
            assentos_disponiveis.append(self.assento)
        self.__assento = novo_assento
        assentos_disponiveis.remove(novo_assento)
    
    # saida de dados
    def __str__(self) -> str:
        saida = f"""
****************Cartão de Embarque****************
Nome: {self.nome}
Numero do Voo: {self.num_voo}
Código da Reserva: {self.cod_reserva}
Data de Embarque: {datetime.strftime(self.data_embarque, "%d/%m/%Y")}
Hora de Embarque: {self.hora_embarque.strftime("%H:%M")}
Check-in: {self.checkin}
Assento: {self.assento}
**************************************************"""
        return saida

# Função Principal
def main():
    assentos_disponiveis = ['A1','A2','A3','B1','B2','B3','C1','C2','C3','D1','D2','D3']
    # print(f"Assentos Disponiveis: {assentos_disponiveis}")
    
    #*********************************01**********************
    c1 = Cartao_Embarque_voo('Silas', 34, "A1B2C3", "29/11/2024", "09:20")
    print(c1)
    c1.check_in(assentos_disponiveis)
    print(c1)
    c1.mudar_assento("A1",assentos_disponiveis)
    print(c1)
    
    # ********************************02**********************
    c2 = Cartao_Embarque_voo('Cynara', 34, "AA22C3", "25/01/2025", "09:20")
    print(c2)
    c2.check_in(assentos_disponiveis)
    print(c2)
    c2.mudar_assento("C3",assentos_disponiveis)
    print(c2)
    
    # ********************************03**********************
    c3 = Cartao_Embarque_voo('Ana', 34, "A1B233", "06/07/2025", "09:20")
    print(c3)
    c3.check_in(assentos_disponiveis)
    print(c3)
    c3.mudar_assento("A2",assentos_disponiveis)
    print(c3)
    
    
if __name__ == "__main__":
    main()