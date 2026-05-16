#Biblioteca

biblioteca = []
emprestimos = []

def mensagem(msg):
    print(msg)

def cadastro_livros():
    nome_livro = input("Nome do livro: ")
    autor_livro = input("Autor do livro: ")
    livro = {
        'nome': nome_livro,
        'autor': autor_livro

    }



    biblioteca.append(nome_livro)
    mensagem("Livro cadastrado com sucesso!")

def mostrar_livros():
    mensagem("\n==== LIVROS ====")
    for i in range(len(biblioteca)):
        mensagem(f"{i} - {biblioteca[i]}")

def emprestimo():
    mostrar_livros()
    escolha = int(input("Escolha o livro pelo número: "))
    emprestimos.append(biblioteca[escolha])
    mensagem("Livro Emprestado com sucesso!")

def total_emprestimo():
    return len(emprestimos)

def menu():
    print("\n ==== BIBLIOTECA PYTHON ====")
    print("1 - Cadastrar Livros")
    print("2 - Mostrar Livros")
    print("3 - Emprestar livros")
    print("4 - Total de empréstimos")
    print("5 - Sair!")

menu()

def main():
    while True:
        menu()
        opcao = int(input("O que deseja fazer?: "))
        if opcao == 1:
            cadastro_livros()
        elif opcao == 2:
            mostrar_livros()
        elif opcao == 3:
            emprestimo()
        elif opcao == 4:
            mensagem(f"Total de empréstimos: {total_emprestimo()}")
        elif opcao == 5:
            mensagem("Saindo...")
            break
        else:
            mensagem("Opção Inválida!")
    
main()