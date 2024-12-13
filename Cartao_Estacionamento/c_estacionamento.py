# IFPI
# CURSO: TDS
# DISCIPLINA: POO
# Exercício Prático - Cartão de Estacionamento de Shopping

# Utilizando o processo de abstração, implemente uma classe em Python que represente um
# cartão de estacionamento de shopping. Identifique atributos mutáveis e imutáveis,
# implemente um construtor da classe e métodos para manipulação dos atributos mutáveis.
# Faça todas as validações possíveis. Utilize encapsulamento nos atributos necessários
# implementando em seguida os decoradores de leitura e/ou escrita. Crie objetos para testar os
# métodos implementados.

# Especificações:

# 1. Atributos:
# - Número do cartão (gerado automaticamente e composto de 8 caracteres alfanuméricos)
# - Data e hora de entrada (registrada automaticamente no momento da criação do cartão)
# - Status do cartão (ativo ou finalizado)
# - Data e hora de saída (registrada quando o cartão é finalizado)
# - Valor total (calculado no momento da saída com base no tempo de permanência e tarifa
# por hora)

# 2. Métodos sugeridos
# - Um método para registrar saída, que define a data e hora de saída, altera o status para
# "finalizado" e calcula o valor total a ser pago.
# - Um método para consultar o valor acumulado, permitindo ao cliente verificar o custo do
# estacionamento antes de finalizar.
# - Um método para calcular o valor a ser pago, condiderando:
# - Até 2h de permanência, R$ 8,00
# - Acima de 2h de permanência cobrar R$ 0,50 a cada fração de 15 min

# 4. Requisitos de Validação:
# - O número do cartão deve ser único e composto de exatamente 5 caracteres numericos.

# - O status só pode ser alterado para "finalizado" se a saída for registrada. 
# - O tempo de permanência deve ser calculado em horas completas e frações, considerando
# uma tarifa fixa por hora.
# - A data e hora de saída não podem ser anteriores à data e hora de entrada.

# 5. Teste:
# - Crie pelo menos três objetos da classe, representando cartões de estacionamento
# diferentes.
# - Demonstre os métodos implementados e suas validações em ação.

# Armazenando os numeros dos cartoes gerados para comparar e garantir não ter iguais
banco_de_dados = []
# importando bibliotecas
import random
import string
from datetime import *
# Inicio da classe Estacionamento
class Estacionamento:
    # contrutor sera inicializado quando o objeto for criado
    def __init__(self) -> None:
        agora = datetime.today()
        # atributos
        self.__num_cartao = self.gerar_cartao()
        self.__data_entrada = agora.date()
        self.__hora_entrada = agora.time()
        self.__status = "Ativo"
        self.__valor_total = None
        self.__data_saida = None
        self.__hora_saida = None
    # decoração
    @property
    def num_cartao(self):
        return self.__num_cartao
    @property
    def data_entrada(self):
        return self.__data_entrada
    @property
    def hora_entrada(self):
        return self.__hora_entrada
    @property
    def status(self):
        return self.__status
    @property
    def valor_total(self):
        return self.__valor_total
    @property
    def data_saida(self):
        return self.__data_saida
    @property
    def hora_saida(self):
        return self.__hora_saida
    # metodo para gerar um sequencia de 8 caracteres com 5 numeros e 3 letras
    def gerar_cartao(self):
        # gerando 5 numeros aleatorios e convertendo para uma string
        numeros = ''.join(random.choices(string.digits, k=5))
        # gerando 3 letras aleatorias 
        letras = ''.join(random.choices(string.ascii_letters, k=3))
        # combinando as duas strings e transformando em um lista
        sequencia = list(numeros + letras)
        # embaralhando os caracteres da lista
        random.shuffle(sequencia)
        # retornando a nova sequencia para o codigo do cartão
        codigo_cartao = ''.join(sequencia)
        # validar se existe no banco de dados, caso exista, gera novamente
        if codigo_cartao in banco_de_dados:
            return self.gerar_cartao()
        # adicionando o codigo gerado a lista para comparações futuras
        banco_de_dados.append(codigo_cartao)
        # saida de dados com o codigo do cartão
        return codigo_cartao
    # metodo que retorna o valor acumulado no momento que o usuario verifica
    def valor_acumulado(self, datetime_atual):
        entrada = datetime.combine(self.__data_entrada, self.__hora_entrada)
        return f"""
Data Atual: {datetime.strftime(datetime_atual, "%d/%m/%Y")}
Hora Atual: {datetime.strftime(datetime_atual, "%I:%M %p")}
Valor Acumulador Ate agora: R$ {self._calcular_valor_total(entrada, datetime_atual):.2f}"""
    # metodo que calcula o valor total a ser pago
    def _calcular_valor_total(self, entrada, saida):
        # Calcula a diferença total em minutos
        diferenca_minutos = int((saida - entrada).total_seconds() // 60)
        # utilizando uma variavel para armazenar 2 horas em minutos 
        hr_base = 120
        # se a diferença em minutos for menor ou igual a 2h convertido para 120 minutos
        if diferenca_minutos <= hr_base:
            # retorna o valor 8
            return 8
        # se não
        else:
            # Calcula o excesso de minutos acima de 2 horas
            excesso_minutos = diferenca_minutos - hr_base
            # Calcula a divisao do excesso pra 15 minutos
            fracao_15_min = excesso_minutos // 15
            # retorna o valor 8 acrescido da fração de 15 minutos vezes 0.50 
            return 8 + (fracao_15_min * 0.50)
    # metodo de check-out saida do estacionamento
    def saida(self, datetime_saida):
        # verifica se a data e hora de saida são menores que a de entrada
        if datetime_saida < datetime.combine(self.__data_entrada, self.__hora_entrada):
            # retornando um erro caso a condição acima seja verdadeiro
            raise ValueError("Data de Saída não pode ser anterior a Data de Entrada")
        # alterando status e atribuido os dados correspondentes aos atributos
        self.__status = "Finalizado"
        self.__data_saida = datetime_saida.date()
        self.__hora_saida = datetime_saida.time()
        # combinando data e hora de entrada 
        entrada = datetime.combine(self.__data_entrada, self.__hora_entrada)
        saida = datetime_saida
        # calculando valor total a ser pago com base na data e horario de entrada e saida
        self.__valor_total = self._calcular_valor_total(entrada, saida)
    # metodo de exibição, exibindo as informações na tela
    def __str__(self) -> str:
        display2 = f"""Data de Saída: {datetime.strftime(self.data_saida, "%d/%m/%Y")}
Horario de Saída: {self.hora_saida.strftime("%I:%M %p")}
Valor Total: R$ {self.valor_total:.2f}
""" if self.data_saida != None else ""
        display = f"""
***********************Cartão de Estacionamento*********************
Número do Cartão: {self.num_cartao}
Data de Entrada: {datetime.strftime(self.data_entrada, "%d/%m/%Y")}
Horario de Entrada: {self.hora_entrada.strftime("%I:%M %p")}
{display2}
Status: {self.status}
******************************************************************
""" 
        return display
# função principal
def main():
    for i in range(3):
        estacionamento = Estacionamento()
        print(estacionamento)
        print(estacionamento.valor_acumulado(datetime.today() + timedelta(hours=2*i, minutes=10)))
        estacionamento.saida(datetime.today() + timedelta(days=2, hours=3*i, minutes=10))
        print(estacionamento)
        print("")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()