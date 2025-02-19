from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(
        label="Nome de usuário:",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}),
    )
    password = forms.CharField(
        label="Insira sua senha:",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
    )

class CadastroForms(forms.Form):
    nome = forms.CharField(
        label="Nome completo:",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo'})
    )
    username = forms.CharField(
         label="Nome de usuário:",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
    )
    email = forms.EmailField(
        label='Digite seu email:',
        required=True,
        max_length=50,
        widget=forms.EmailInput(
            attrs={'placeholder':'Insira seu email'}
        )
    )
    password = forms.CharField(
        label="Insira sua senha:",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
    )
    password2 = forms.CharField(
        label="Insira sua senha:",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
    )