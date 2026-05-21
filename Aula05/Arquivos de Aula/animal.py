class Animal:
    def __init__(self,nome_animal, idade_animal, raca_animal, tipo_animal, som_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        self.raca = raca_animal
        self.tipo = tipo_animal
        self.som = som_animal
 
    def desc_animal(self):
        print(f'O animal {self.nome},\n a idade é {self.idade},\n raça:{self.raca}')
 
    def emitir_som(self):
        mensagem = print(f'O animal {self.nome}, faz {self.som}')
        return mensagem
   
cachorro = Animal('Amora','3 meses','bulldog','cachorro','Au Au')

cachorro.desc_animal()

cachorro.emitir_som()

print(30*"-")

gato = Animal("Pepe", "12 anos", "vira lata", "gato", "Miau")
gato.desc_animal
print(gato.emitir_som())