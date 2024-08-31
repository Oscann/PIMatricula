from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()

    context = {
        "alunos": alunos
    }

    return render(request, 'index.html', context)

def cadastro(request):
    if request.method == 'POST':
        post_form = AlunoForm(request.POST)

        if post_form.is_valid():
            Aluno.objects.create(**post_form.cleaned_data)

            return redirect(to='/')

    form = AlunoForm()

    context = {
        "form": form
    }

    return render(request, 'cadastro.html', context)