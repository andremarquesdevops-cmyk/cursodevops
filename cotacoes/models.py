from django.db import models


class Cotacao(models.Model):
	TIPO_SEGURO_CHOICES = [
		('auto', 'Seguro Auto'),
		('residencial', 'Seguro Residencial'),
		('vida', 'Seguro de Vida'),
		('saude', 'Seguro Saude'),
		('viagem', 'Seguro Viagem'),
	]

	nome = models.CharField(max_length=120)
	email = models.EmailField()
	telefone = models.CharField(max_length=20)
	cidade = models.CharField(max_length=120)
	tipo_seguro = models.CharField(max_length=20, choices=TIPO_SEGURO_CHOICES)
	mensagem = models.TextField(blank=True)
	criado_em = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-criado_em']
		verbose_name = 'Cotacao'
		verbose_name_plural = 'Cotacoes'

	def __str__(self):
		return f'{self.nome} - {self.get_tipo_seguro_display()}'
