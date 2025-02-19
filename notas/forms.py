from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'categoria', 'conteudo']  
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da nota'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite sua nota aqui...', 'rows': 5}),
        }
