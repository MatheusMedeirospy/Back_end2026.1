def calculo(valor_um,operador,valor_dois):
    if operador == "+":
        resultado = valor_um + valor_dois
        return resultado
    elif operador == "-":
        resultado = valor_um - valor_dois
        return resultado
    elif operador == "*":
        resultado = valor_um * valor_dois
        return resultado
    elif operador == "/":

        
        if valor_dois == 0:
            
            mensagem = "Não é possivel divisão por zero!"
            return mensagem
        else:
            resultado = valor_um / valor_dois
            return resultado

def main():
    print("Bem vindo(a) a calculadora do Python\n")
    print(30*"=")

    numero_um = int(input("Informe o primeiro valor: "))
    op = input("Informe a operação [+] [-] [*] [/]: ")
    numero_dois = int(input("Informe o segundo valor: "))

    print(f"O resultado é: {calculo(numero_um,op,numero_dois)}")

main()
