from django.contrib import admin

from .models import Cotacao


@admin.register(Cotacao)
class CotacaoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone', 'cidade', 'tipo_seguro', 'criado_em')
	search_fields = ('nome', 'email', 'telefone', 'cidade')
	list_filter = ('tipo_seguro', 'criado_em')
