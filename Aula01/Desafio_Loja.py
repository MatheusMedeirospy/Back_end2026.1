print(33*"-")
print("Bem vindo a Loja de Games Python!")
print(33*"-")
print("Estes são os jogos disponíveis!\n")
print("JOGOS: \n")
disponiveis = "Minecraft - R$80 \nGTA V - R$120 \nFIFA - R$90"
print(disponiveis)

minecraft = 80
gtav = 120
fifa = 90


qtd = 0
valor = 0

while True:
    compra = input("\n""Qual jogo gostaria de comprar ?""\n""Optando por encerrar o atendimento, basta digitar SAIR""\n").lower()


    if compra == "sair":
        print(f"Sua compra ficou com {qtd} games e no valor de R${valor}!")
        if valor > 200:
            desconto = valor * 0.10
            descontofinal = valor - desconto
            print(f"Como sua compra passou de R$200, você ganhou um desconto de 10%, sua compra que ficaria no valor de R${valor}\n com o desconto ficou por apenas R${descontofinal} ")
        break
    if compra == "minecraft":
        qtd = qtd + 1
        valor = valor + minecraft
        print(f"Seu carrinho contém {qtd} e este é o valor atual das suas compras {valor} ")
    if compra == "gtav" or compra == "gta":
        qtd = qtd + 1
        valor = valor + gtav
        print(f"Seu carrinho contém {qtd} e este é o valor atual das suas compras {valor} ")
    if compra == "fifa":
        qtd = qtd + 1
        valor = valor + fifa
        print(f"Seu carrinho contém {qtd} e este é o valor atual das suas compras {valor} ")

    else:
        print("Caractér Inválido! Tente Novamente.")


    
        
