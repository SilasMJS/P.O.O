from datetime import datetime

class Carteira_habilitação:
    def __init__(self, nome, cpf, data_nasc, cat_Hab, data_emissao,validade, observacao = "") -> None:
        # os Métodos validadores serão chamados aqui...
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = self.valida_data(data_nasc)
        self.cat_Hab = self.valida_tipo_CNH(cat_Hab)
        self.data_emissao = self.valida_data(data_emissao)
        self.validade = self.validade_CNH(validade)
        self.observacao = observacao
        
    def validade_CNH(self, validade):
        # Atribuindo validade de acordo com a data de emissao de forma automatica
        # self.idade = datetime.today().year - int(datetime.strftime(self.data_nasc, "%Y"))
        # validade = self.valida_data(self.data_emissao)
        # if(self.idade < 50):
        #     validade = validade.replace(year = validade.year + 10)
        # else:
        #     validade = validade.replace(year = validade.year + 5)
        # validade = datetime.strftime(validade, "%d/%m/%Y")
        # return validade
        
        # validando a validade e verificando se não é inferior a data de emissao
        validade = self.valida_data(validade)
        if(validade.year > self.data_emissao.year):
            return datetime.strftime(validade, "%d/%m/%Y")
        else:
            raise ValueError("Vencimento Inválido!")
        
    def valida_data(self, data):
        # converter a string data em um tipo date/datetime
        # se a conversão falhar, levantar uma exceção (raise ValueErro(<mensagem>))
        # se a conversão passar, retornar a data convertida
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data Inválida!")
    
    def valida_tipo_CNH(self, tipo):
        # verificar se o tipo está entre o conjunto válido de CNHs
        # se sim retornar o Tipo, senão levantar uma exceção
        tipo = tipo.upper()
        if(tipo in ("A","AB","AC","AD","B","BC","BD","C","CD","D")):
            return tipo
        else:
            raise ValueError("Tipo da Categoria Inválido!")
    
    def renovar_CNH(self):
        # se idade < 50, renovar por 10anos
        # senão, renovar por 5 anos
        self.idade = datetime.today().year - int(datetime.strftime(self.data_nasc, "%Y"))
        self.nova_validade = datetime.today()
        if(self.idade < 50):
            self.nova_validade = self.nova_validade.replace(year = self.nova_validade.year + 10)
        else:
            self.nova_validade = self.nova_validade.replace(year = self.nova_validade.year + 5)
        self.validade = datetime.strftime(self.nova_validade, "%d/%m/%Y")
        self.data_emissao = datetime.today()
        return "Habilitação Renovada Com Sucesso!"
    
    def mudar_categoria_CNH(self, nova_categoria):
        # verificar se nova_categoria é uma categoria válida
        # verificar se é possível a mudança
        # se sim, alterar o atributo senão, exibir uma mensagem de erro!
        # nova_categoria = nova_categoria.upper()
        nova_categoria = self.valida_tipo_CNH(nova_categoria)
        # if(nova_categoria in ("A","AB","AC","AD","B","BC","BD","C","CD","D")):
        if(nova_categoria > self.cat_Hab):
            # self.cat_Hab += ", " + nova_categoria
            self.cat_Hab = nova_categoria
            return f"Categoria Mudada Com Sucesso! Categoria: {nova_categoria}" 
        else:
            raise ValueError("Mudança para Categoria Inverior Não Permitida!")
        # else:
            # raise ValueError("Tipo da Categoria Inválido!")
    
    def __str__(self) -> str:
        # retornar uma string com os dados da carteira de habilitação
        saida = f"""
**********************Carteira de Habilitação**********************
Nome: {self.nome}
CPF: {self.cpf}
Data de Nascimento: {datetime.strftime(self.data_nasc, "%d/%m/%Y")}
Categoria da Habilitação: {self.cat_Hab}
Validade: {self.validade}
Data de Emissão: {datetime.strftime(self.data_emissao, "%d/%m/%Y")}
Observação: {self.observacao}
*******************************************************************
        """
        return saida
    
c1 = Carteira_habilitação("Silas", "000.000.000-00", '06/07/2000', 'A', '09/10/2020', '09/10/2030')
print(c1)
c2 = Carteira_habilitação("Irmão", "000.000.000-00", '01/05/2002', 'a', '09/10/2023', '09/10/2033')
print(c2)
print(c2.mudar_categoria_CNH("b"))
print(c2)
print(c1.renovar_CNH())
print(c1)
# print(datetime.today().year - int(datetime.strftime(c1.data_nasc, "%Y")))
# print(int(datetime.strftime(c1.data_nasc, "%Y")))
print(c2.renovar_CNH())
print(c2)