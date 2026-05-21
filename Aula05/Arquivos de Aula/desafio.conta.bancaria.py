class ContaBancaria:
    def __init__(self):
        self.__saldo = 0 #Atributo Privado (Só pode ser alterado através do método!)
        self.titular = ""

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso")
        else:
            print("Valor de deposito invalido!")

    def saque(self, valor_saque):
        if valor_saque > 0 and valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
            print(f"Saque de R${valor_saque} realizado com sucesso!")
        else:
            print("Saldo Insuficiente ou Valor Inválido!")

    def consulta_saldo(self):
        print(f"Titular: {self.titular}\nSaldo Atual R${self.__saldo}")

    def main(self):
        nome_cliente = input("Informe o Nome do Titular da Conta: ")
        while True:
            opcao = int (input("Escolha uma opção:\n[1 - Depositar]\n[2 - Sacar]\n[3 - Mostrar Saldo]\n[4 - Sair]"))
            
            self.titular = nome_cliente

            if opcao == 1:
                valor = float(input("Informe o valor de depósito R$"))
                self.depositar(valor)
            elif opcao == 2:
                valor = float(input("Informe o valor de depósito R$"))
                self.saque(valor)
            elif opcao == 3:
                self.consulta_saldo
            elif opcao == 4:
                print(f"Encerrando a sessão! Até breve Sr{self.titular} ")
                break
            else:
                print("Opção Inválida!")
                

cliente = ContaBancaria()
cliente.main()