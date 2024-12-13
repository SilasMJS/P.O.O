import sys
import os 
class Calculadora:
    total = 0
    num = 0
    op = None
    ligado = False
    
    def ligar(self):
        self.ligado = True
        print('Calculadora Ligada!')
        
    def desligar(self):
        self.ligado = False
        print('Calculadora Desligada!')
    
    def reset(self):
        self.total = 0
        self.num = 0
        self.op= None
    
    def obter_numero(self):
        return float(input('Digite um Numero: '))
    
    def obter_operacao(self):
        return input('Pressione uma das seguinte Operações ( +, -, *, /) ')
    
    def calcular(self, num1, num2, op):
        if op == "+":
            return num1 + num2
    
        if op == "-":
            return num1 - num2
    
        if op == "*":
            return num1 * num2
    
        if op == "/":
            return num1 / num2
    
    def interface(self):
        if self.ligado == False:
            opc = input("Calculadora Desligada! Deseja Ligar? (pressione - L) (Sair - S) ").upper()
            if opc == 'L':
                self.ligar()
                while True:
                    self.total = self.obter_numero()
                    while True:
                        self.op = self.obter_operacao()
                        if self.op in "+-*/":
                            while True:
                                self.num = self.obter_numero()
                                if self.num != 0:
                                    self.total = self.calcular(self.total, self.num, self.op)
                                    print(self.total)
                                    opc = input('continuar? S-(sim) N-(não) C-(Clear) ').upper()
                                    if opc == 'N':
                                        break
                                    if opc == 'C':
                                        self.reset()
                                        os.system('cls')
                                        break
                                    else:
                                        break
                                else:
                                    print('Erro: Divisor não pode ser zero!')
                        else:
                            print('operação invalida!')
                        if opc == "C":
                            break
                        if opc == 'N':
                            self.desligar()
                            break
                    if opc == 'N':
                        break
            else:
                self.desligar()

def main():
    app = Calculadora()
    
    app.interface()
    
if __name__ == "__main__":
    main()