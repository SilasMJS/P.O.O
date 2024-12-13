import sys
import os

class Calculadora:

    def somar(self, num1, num2):

        return num1 + num2

    def multiplicar(self, num1, num2):
        
        return num1 * num2
    
    def dividir(self, num1, num2):
        return num1 / num2

    def subtrair(self, num1, num2):
        return num1 - num2


class Display:

    def menu(self):
        print('''numero: ''')

    def menu_operacao(self):
        print(''' + - / * = ''')


    def imprimir_resultado(self, num):
        print(num)


class App:

    def __init__(self) -> None:
        self.display = Display()
        self.calculadora = Calculadora()

        self.total = False

        self.num = 0

    def init(self):

        while True:
            if self.total == False:
                self.num = self.selecionar_numero()

            op = self.selecionar_operacao()
            if self.total == False:
                self.total = self.num

                # self.num = 0

            self.num = self.selecionar_numero()


            if op:
                self.total = op(self.total, self.num)
                
            self.display.imprimir_resultado(self.total)


    def selecionar_numero(self):
        self.display.menu()

        return float(input(''))


    def selecionar_operacao(self):
        self.display.menu_operacao()
        
        op = input('')

        if op == '+':
            return self.calculadora.somar
        elif op == '-':
            return self.calculadora.subtrair
        elif op == '*':
            return self.calculadora.multiplicar
        elif op == '/':
            return self.calculadora.dividir
        elif op == '=':
            self.display.imprimir_resultado(self.total)
            sys.exit()
        else:
            raise Exception('operação invalida')


def main():
    app = App()

    app.init()    

if __name__ == '__main__':
    main()