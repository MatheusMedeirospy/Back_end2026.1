def mensagem(msg):
    print(msg)


class Jogo():
    def __init__(self, nome, categoria, preco):
        self.nome_jogo = nome
        self.categoria_jogo = categoria
        self.preco_jogo = preco

    def mostrar_dados(self):
        mensagem(f"Nome do Jogo {self.nome_jogo}\nCategoria: {self.categoria_jogo}\nPreço: {self.preco_jogo}")



class Loja():
    def __init__(self):
        self.lista_jogos = []

    def cadastrar_jogo(self):
        while True:
                try:
                    nome_cadastro = input("Informe o nome do jogo:  ")
                    categoria_cadastro = input("Informe a categoria do jogo:  ")
                    preco_cadastro = input("Informe o preço do jogo:  ")

                    novo_jogo = Jogo(nome_cadastro, categoria_cadastro, preco_cadastro)
                    self.lista_jogos.append(novo_jogo)
                    mensagem("Cadastro realizado com sucesso!")
                    mensagem(self.lista_jogos)  

                    while True:
                            opcao = input("Deseja realizar outro cadastro?")
                            if opcao in ['sim','s']:
                                continue
                            elif opcao in ['não', 'nao', 'n']:
                                break
                            else:
                                mensagem("Opção inválida!")
                                continue
                except ValueError:
                    mensagem("Opção Inválida.")

