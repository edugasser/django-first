import django_tables2 as tables
from personas.models import Ficha_Persona

class PersonaTable(tables.Table):
	control = tables.Column(sortable=False)
	control = tables.TemplateColumn('<a href="/edit/{{record.pk}}">Editar</a>')

	class Meta:
		model = Ficha_Persona
		# add class="paleblue" to <table> tag
		attrs = {"id": "tutorial" ,"class": "paleblue"}
		fields = ('nombre', 'apellido', 'control') # fields to display
