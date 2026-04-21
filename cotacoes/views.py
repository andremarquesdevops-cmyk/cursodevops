from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from .forms import CotacaoForm, LoginVendedorForm
from .models import Cotacao


class CadastroCotacaoView(View):
	template_name = 'cotacoes/cadastro.html'

	def get(self, request):
		form = CotacaoForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = CotacaoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Cadastro enviado com sucesso. Em breve entraremos em contato.')
			return redirect('cadastro_cotacao')

		return render(request, self.template_name, {'form': form})


class LoginVendedorView(View):
	template_name = 'cotacoes/login.html'

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('painel_cotacoes')

		form = LoginVendedorForm(request)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		if request.user.is_authenticated:
			return redirect('painel_cotacoes')

		form = LoginVendedorForm(request, data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			return redirect('painel_cotacoes')

		return render(request, self.template_name, {'form': form})


@method_decorator(login_required(login_url='login_vendedor'), name='dispatch')
class PainelCotacoesView(View):
	template_name = 'cotacoes/painel.html'

	def get(self, request):
		busca = request.GET.get('busca', '').strip()
		cotacoes = Cotacao.objects.all()

		if busca:
			cotacoes = cotacoes.filter(nome__icontains=busca)

		context = {
			'cotacoes': cotacoes,
			'busca': busca,
			'total_cotacoes': cotacoes.count(),
		}
		return render(request, self.template_name, context)


class LogoutVendedorView(View):
	def get(self, request):
		logout(request)
		return redirect('login_vendedor')
