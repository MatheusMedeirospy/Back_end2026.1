#A palavra class é a palavra reservada para criar uma classe
#A classe é um molde do objeto
#Iniciar o nome da classe com letra MAIÚSCULA!

class Carro:
    #Método =
    #self representa o proprio metodo e seus elementos
    def buzinar(self):
        print("BIBIBI")

    def andar(self):
        print("Em Movimento!")

#Cria o objeto utilizando a classe(Molde)
carro_um = Carro() #Instanciar a classe
carro_um.buzinar()
carro_um.andar()