class Bicicleta:
    # Limites
    altura_min = 5
    altura_max = 10
    min_calib = 20
    max_calib = 40
    velc_min = 0.1
    veloc_max = 20
    # construtor
    def __init__(self) -> None:
        self.veloc_atual = 0
        self.altura_cela = 5
        self.calibragem = 30
    # metodo
    def acelerar(self):
        if self.veloc_atual < self.veloc_max: 
            self.veloc_atual += 1
            return 'Acelerando...'
        return 'Velocidade Máxima!'
    # metodo
    def frear(self, forca_freio):
        self.veloc_atual -= forca_freio
        if self.veloc_atual < self.velc_min:
            self.veloc_atual = 0
        return 'Freando...'
    # metodo
    def regular_cela(self, nova_altura):
        if self.veloc_atual == 0:
            if self.altura_min <= nova_altura <= self.altura_max:
                self.altura_cela = nova_altura
                return f'Altura da cela ajustada para {self.altura_cela} cm'
            else:
                return 'Erro: Altura da cela fora dos limites.'
        else:
            return 'Pare a Bicicleta Primeira antes de regular a cela!'
    # metodo
    def calibrar(self, nova_calibragem):
        if self.veloc_atual == 0:
            if self.min_calib <= nova_calibragem <= self.max_calib and nova_calibragem > self.calibragem:
                self.calibragem = nova_calibragem
                return f'Pneus calibrados para {self.calibragem}'
            else:
                return 'Erro: Calibragem fora dos limites.'
        else:
            return 'Pare a Bicicleta Primeira antes de calibrar os pneus!'
# instancia de objeto
bici = Bicicleta()
for a in range(30):
    acelerar = bici.acelerar()
    if acelerar != 'Velocidade Máxima!':
        print(acelerar)
    else:
        break
print(bici.regular_cela(5.3))
print(bici.calibrar(25))
print(bici.veloc_atual)
print(bici.frear(2))
print(bici.veloc_atual)
print(bici.frear(20))
print(bici.veloc_atual)
print(bici.regular_cela(5.3))
print(bici.calibrar(35))
