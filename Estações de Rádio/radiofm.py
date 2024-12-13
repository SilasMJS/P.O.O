# - Implementar encapsulamento nesse código
# - Implemente todos os métodos descritos acima:
# • No método ligar, atualizar o atributo ligado para True, o volume do
# rádio deverá ser inicializado com o volume mínimo do rádio. Se a antena estiver habilitada
# (antena_habilitada=True), a frequencia deverá ser inicializada com a
# frequencia da primeira estação de rádio definida no dicionário e a estação
# atual deverá ser inicializada com seu respectivo nome.

# • No método desligar, mudar o estado para False, além de atualizar os
# atributos: volume, frequencia_atual e estação_atual para: None

# • O método aumentar_volume deverá receber um atributo opcional com valor
# inicial igual a 1. Caso este valor seja passado na chamada do argumento,
# atualizar o volume com o valor do argumento (fazer a crítica para não
# ultrapassar os valores permitidos para o volume). Caso o argumento fique
# vazio na chamada, o atributo volume deverá ser incrementado de uma
# unidade. (Fazer a crítica para não ultrapassar o valor máximo permitido)

# • Idem para o método: diminur_volume

# • O método mudar_frequencia deverá receber um atributo opcional com valor
# inicial igual a 0. Caso seja passado um valor para a frequencia na chamada
# deste método, atualizar o atributo frequencia_atual para o valor passado no
# argumento. Se o valor da frequencia estiver presente no dicionário, atualizar o
# atributo: estação_atual com o nome da respectiva frequencia que se encontra
# no dicionário, caso contrário atualizar com o valor: ‘estação inexistente’. Caso
# este método seja chamado sem argumentos, atualizar a frequencia_atual com
# a frequência referente ao próximo elemento do dicionário e atualizar o
# atributo: estação_atual com seu respectivo nome. Se a frequencia atual for
# igual ao último elemento do dicionário, mudar os atributos: frequencia e
# estação para os respectivos valores referentes ao primeiro elemento do
# dicionário.

# • Criar pelo menos 3 objetos e testar os métodos implementados.

estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa' , 99.1: 'Clube'}
class RadioFM:
    def __init__(self, vol_max, estacoes) -> None:
        self.__volume_min = 0
        self.volume_max = vol_max
        self.__freq_min = 88
        self.__freq_max = 108
        self.estacoes = estacoes
        self.__volume = None
        self.__ligado = False
        self.estacao_atual = None
        self.__frequencia_atual = None
        self.antena_habilitada = False
    
    @property
    def volume_min(self):
        return self.__volume_min
    
    @property
    def freq_min(self):
        return self.__freq_min
    
    @property
    def freq_max(self):
        return self.__freq_max
    
    @property
    def volume(self):
        return self.__volume
    
    @property
    def ligado(self):
        return self.__ligado
    
    @property
    def frequencia_atual(self):
        return self.__frequencia_atual
    
    
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            self.__volume = self.__volume_min
            if (self.antena_habilitada):
                self.__frequencia_atual = list(self.estacoes.keys())[0]
                self.estacao_atual = self.estacoes[self.frequencia_atual]
        else:
            raise ValueError("Radio Ja está Ligado!")
    
    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            self.__volume = None
            self.__frequencia_atual = None
            self.estacao_atual = None
        else:
            raise ValueError("Radio ja está Desligado!")
    
    def habilitar_desabiliar(self):
        if not self.__ligado:
            if self.antena_habilitada:
                self.antena_habilitada = False
            self.antena_habilitada = True
        else:
            raise ValueError("Desligue o Radio para Habilitar ou Desabilitar a Antena")
    
    def aumentar_volume(self, valor = 1):
        if self.__ligado:
            self.__volume += valor
            if (self.__volume > self.volume_max):
                self.__volume = self.volume_max
        else:
            raise ValueError("Radio Desligado!")
    
    def diminuir_volume(self, valor = 1):
        if self.__ligado:
            self.__volume -= valor
            if (self.volume < self.__volume_min):
                self.__volume = self.__volume_min
        else:
            raise ValueError("Radio Desligado!")
    
    def mudar_frequencia(self, valor = 0):
        if self.__ligado:
            if valor == 0:
                lista_freq = list(self.estacoes.keys())
                indice_atual = lista_freq.index(self.frequencia_atual)
                indice_prox = (indice_atual + 1) % len(lista_freq)
                self.__frequencia_atual = lista_freq[indice_prox]
            else:
                self.__frequencia_atual = valor
            self.estacao_atual = self.estacoes.get(self.__frequencia_atual, 'Estação Inexistente')
        else:
            raise ValueError("Radio Desligado!")
        
    def __str__(self) -> str:
        display = f"""
Ligado!
Frequencia E Estações {self.estacoes}
Frequencia Atual: {self.frequencia_atual}
Estação Atual: {self.estacao_atual}
Volume: {self.volume}
Antena: {"Habilitada!" if self.antena_habilitada else "Desabilitada!"}
""" if self.ligado else """
Desligado!
"""
        return display
    
def main():
    
    radio1 = RadioFM(10, estacoes)
    print(radio1)
    radio1.habilitar_desabiliar()
    radio1.ligar()
    print(radio1)
    for i in range(16):
        radio1.aumentar_volume()
    print(radio1)
    for i in range(16):
        radio1.diminuir_volume()
    print(radio1)
    radio1.mudar_frequencia(94.1)
    print(radio1)
    
    
    radio2 = RadioFM(20, estacoes)
    print(radio2)
    radio2.habilitar_desabiliar()
    radio2.ligar()
    print(radio2)
    for i in range(16):
        radio2.aumentar_volume()
    print(radio2)
    for i in range(16):
        radio2.diminuir_volume()
    print(radio2)
    radio2.mudar_frequencia(89.5)
    print(radio2)
    
    
    radio3 = RadioFM(15, estacoes)
    print(radio3)
    radio3.habilitar_desabiliar()
    radio3.ligar()
    print(radio3)
    for i in range(16):
        radio3.aumentar_volume()
    print(radio3)
    for i in range(16):
        radio3.diminuir_volume()
    print(radio3)
    radio3.mudar_frequencia(99.1)
    print(radio3)

if __name__ == "__main__":
    main()