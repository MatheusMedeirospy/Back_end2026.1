from django.shortcuts import render

# Create your views here.

def dados_alunos(request):
    titulo = 'Informações dos Alunos'
    info_alunos = [

        {'nome': 'Matheus', 'curso': 'Python', 'turma': '2026.1'},
        {'nome': 'Lucas', 'curso': 'Java', 'turma': '2026.2'},
        {'nome': 'Marcos', 'curso': 'CSS', 'turma': '2026.3'}
    ]
    return render(request,'cadastros/cad_alunos.html',{'alunos':info_alunos, 'msg':titulo})