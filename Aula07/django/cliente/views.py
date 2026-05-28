from django.shortcuts import render #Ja vem por padrão

#Importar a classe (Ferramenta) HttpReponse
from django.http import HttpResponse #Vai responder a solicitação do navegador


#Cria a função que responde a solicitação do navegador
def ola_mundo(request):
    return HttpResponse ("<h1>Ola Mundo!<h1>  <p>ola django</p>")

def contato(request):
    return render (request,"clientes/contato.html")


#Chamar arquivos HTML (Template)
def home(request):
    #conceito de context (contexto)
    #Context - pega dados na view e passa para o template.
    titulo = "Nossos clientes"
    nosso_cliente = {
        'nome': "Matheus",
        'idade' : 28,
        'nascimento': "23/12/1997"

    }

    nomes_clientes = ["Maria","Joao","Matheus","Ana"]

    carros = [

        {'marca': "Chevrolet", 'modelo': 'Onix LT','ano': "2020"},
        {'marca': "Fiat", 'modelo': 'Uno','ano': "2010"}


    ]

    return render (request, "clientes/home.html", {'mensagem':titulo, 'lista_clientes':nosso_cliente, 'dados':nomes_clientes, 'meus_carros': carros})