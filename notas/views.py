from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from notas.models import Nota
from notas.forms import NotaForm


@login_required
def listar_notas(request):
    notas = Nota.objects.filter(usuario=request.user)  
    return render(request, 'notas/listar_nota.html', {'notas': notas})


@login_required
def criar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.usuario = request.user 
            nota.save()
            return redirect('listar_nota')  

    else:
        form = NotaForm()

    return render(request, 'notas/criar_nota.html', {'form': form})