""" Crie uma lista que guarde as armas do jogo """

""" Lista ou Arreio (Python) """
inventario= ["Espada", "Poção", "Escudo"]

""" Adiciona mais itens """

inventario.append("Lança")

print("Aqui esta seu inventario:")
for i in inventario:
    print(i)


""" A tupla é imutável """

valor_ataque = (10, 20)

valor_ataque.append(30)