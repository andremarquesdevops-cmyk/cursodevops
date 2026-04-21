from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Cotacao


class CotacaoForm(forms.ModelForm):
    class Meta:
        model = Cotacao
        fields = [
            'nome',
            'email',
            'telefone',
            'cidade',
            'tipo_seguro',
            'mensagem',
        ]
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 4}),
        }


class LoginVendedorForm(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
