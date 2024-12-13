class Calculadora:
    num1 = 0
    num2 = 0
    op = None
    
    def calcular(self, num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        
        if self.op == '+':
            return self.num1 + self.num2
        elif self.op == '-':
            return self.num1 - self.num2
        elif self.op == '*':
            return self.num1 * self.num2
        elif self.op == '/':
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Erro: Divisão por zero não permitida"
        else:
            return "Operação Inválida!"
    

def main():
    m_calc = Calculadora()
    while True:
        try:
            n1 = float(input("Digite o Primeiro Número: "))
            op = input("Escolha a Operação (+, -, *, /) ou 'q' para sair: ")
            if op == 'q':
                print("Saindo...")
                break
            n2 = float(input("Digite o Segundo Número: "))
            
            result = m_calc.calcular(n1, n2, op)
            print(f'{n1} {op} {n2} = {result}')
            
            while True:
                op = input("Deseja Continuar? Digite (=) ou 'q' para Começar um Novo Calculo: ")
                if op == 'q':
                    print("Saindo...")
                    break
                if op == '=':
                    print(f'{result}')
                    op = input("Escolha a Operação (+, -, *, /) ou 'q' para Começar um Novo Calculo: ")
                    if op == 'q':
                        print("Saindo...")
                        break
                    n2 = float(input("Digite o Segundo Número: "))

                    n_result = m_calc.calcular(result, n2, op)
                    print(f'{result} {op} {n2} = {n_result}')
                    result = n_result            
        except ValueError:
            print("Por favor, Digite valores númericos válidos. ")
    
    
if __name__ == "__main__":
    main()