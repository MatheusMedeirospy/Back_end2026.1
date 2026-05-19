class Aluno:

    #Metodo Construtor(Tudo que tiver dentro dele sera criado automaticamente quando a classe for usada)
    #O metodo _init_ é um método padrão
    def __init__(self, nome_aluno, idade_aluno):

        #Atributos - Variaveis metidas
        self.nome = nome_aluno
        self.idade = idade_aluno

    def estudar(self):
        print(f"{self.nome}, Estudando Python")

aluno_um = Aluno("Matheus", 28) #Instancia

print(f"Nome: {aluno_um.nome}")
print(f"Idade: {aluno_um.idade}")

aluno_dois = Aluno("Maria", 56)

print(f"Nome: {aluno_dois.nome}")
print(f"Idade: {aluno_dois.idade}")

print(20*"-")

nome = input("Informe o nnome do primeiro aluno:")
idade = int(input("Informe a idade:"))

aluno_tres = Aluno(nome,idade)
print(f"Nome: {aluno_tres.nome}")
print(f"Idade: {aluno_tres.idade}")
aluno_tres.estudar()