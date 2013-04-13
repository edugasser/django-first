from django.db import models
from django.utils.formats import get_format
import datetime
# Create your models here.
class Ficha_Persona(models.Model):
	## ESTADO CIVIL 
	CASADO_ESTADO = 1
	SOLTERO_ESTADO = 2
	DIVORCIADO_ESTADO = 3
	SEPARADO_ESTADO = 4
	UNION_ESTADO = 5
	ESTADO_CIVIL = (	 
		(CASADO_ESTADO, 'Casado/a'),
		(SOLTERO_ESTADO, 'Soltero/a'),
		(DIVORCIADO_ESTADO, 'Divorciado/a'),
		(SEPARADO_ESTADO, 'Separado/a'),
		(UNION_ESTADO, 'Union libre')
		)
	# SEXO
	HOMBRE_SEXO = 1
	MUJER_SEXO = 2
	SEXO = (
		(HOMBRE_SEXO, 'Hombre'),
		(MUJER_SEXO, 'Mujer')
		)
	short_datetime_format = get_format("SHORT_DATETIME_FORMAT")
	## Campos tabla
	nombre = models.CharField(max_length=250,blank=False)
	apellido = models.CharField(max_length=250, blank=False)
	fecha_nacimiento = models.DateField(blank=True,null=True)
	pais_origen = models.CharField(max_length=100, blank=True)
	poblacion_actual = models.CharField(max_length=100, blank=True)
	estado_civil = models.IntegerField(choices=ESTADO_CIVIL, blank=True, null=True)
	sexo = models.IntegerField(choices=SEXO, default=1)
	dni = models.CharField(max_length=9, help_text='Escriba todo junto y sin guiones', unique=True, blank=True, null=True)
	es_miembro = models.BooleanField(default=False)
	fecha_miembro = models.DateField(blank=True, null=True)
	formacion = models.CharField(max_length=200, blank=True)
	empleo = models.CharField(max_length=200, blank=True)
	email = models.EmailField(blank=True)
	telefono = models.CharField(max_length=9, blank=True)
	movil = models.CharField(max_length=9, blank=True)
	direccion = models.CharField(max_length=300, blank=True)
	imagen = models.ImageField(upload_to='fotos', verbose_name='Imagen perfil', blank=True, null=True)
	#added_by = models.IntegerField(User.id)
	added_at = models.DateTimeField(verbose_name='Registrado el:', auto_now_add=True)
	update_at = models.DateTimeField(verbose_name='Actualizado el:',auto_now_add=True)
	info_extra = models.ManyToManyField('Info_Extra', null=True, blank=True)
	
	def __unicode__(self):
		return self.nombre +" "+ self.apellido

	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "Fichas"

	def get_absolute_url(self):
		return "/ficha/%s/" % self.id


class Info_Extra(models.Model):
	titulo = models.CharField(max_length=250, blank=False, null=False)
	tipo = models.ForeignKey('Tipo_Info_Extra')
	added_at = models.DateTimeField(verbose_name='Creado el: ', auto_now_add=True)
	update_at = models.DateTimeField(verbose_name='Modificado el: ', auto_now_add=True)

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['titulo']
		verbose_name_plural = 'Informacion extra'

class Tipo_Info_Extra(models.Model):
	titulo = models.CharField(max_length=100, blank=False, null=False)

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['titulo']
		verbose_name_plural = 'Tipo informacion extra'

class Congregacion(models.Model):
	nombre_congregacion = models.CharField(max_length=100, blank=False, null=False)

	def __unicode__(self):
		return self.nombre_congregacion

	class Meta:
		ordering = ['nombre_congregacion']
		verbose_name_plural = 'Congregaciones'

class Tipo_Grupo(models.Model):
	tipo_grupo = models.CharField(max_length=100, blank=False, null=False)

	def __unicode__(self):
		return self.tipo_grupo

	class Meta:
		ordering = ['tipo_grupo']
		verbose_name_plural = 'Tipos de grupos'

class Lugar_Reunion(models.Model):
	nombre_lugar = models.CharField(max_length=100, blank=False, null=False)
	direccion_lugar = models.CharField(max_length=200, blank=True, null=True)
	telefono_lugar = models.CharField(max_length=9, blank=True, null=True)
	id_congregacion = models.ForeignKey('Congregacion')

	def __unicode__(self):
		return self.nombre_lugar

	class Meta:
		ordering = ['nombre_lugar']
		verbose_name_plural = 'Lugares de reunion'
		

class Grupo(models.Model):
	LUNES = 1
	MARTES = 2
	MIERCOLES = 3
	JUEVES = 4
	VIERNES = 5
	SABADO = 6
	DIAS = (
		(LUNES, 'Lunes'),
		(MARTES, 'Martes'),
		(MIERCOLES, 'Miercoles'),
		(JUEVES, 'Jueves'),
		(VIERNES, 'Viernes'),
		(SABADO, 'Sabado')
		)
	id_responsable = models.ForeignKey('Ficha_Persona', related_name="responsable_grupo")
	id_anfitrion = models.ForeignKey('Ficha_Persona', related_name="anfitrion_grupo", blank=True)
	id_tipo_grupo = models.ForeignKey('Tipo_Grupo', blank=False,null=False)
	dia_grupo = models.IntegerField(choices=DIAS, blank=True, null=True)
	hora_grupo = models.CharField(max_length="5", blank=True, null=True)
	id_congregacion = models.ForeignKey('Congregacion', blank=True, null=True)
	id_lugar_reunion = models.ForeignKey('Lugar_Reunion', blank=True,null=True)
	visibilidad = models.BooleanField(default=False)
	update_at = models.DateTimeField(verbose_name='Modificado el: ', auto_now_add=True)
	added_at = models.DateTimeField(verbose_name='Modificado el: ', auto_now_add=True)
	update_anfitrion_at = models.DateTimeField(verbose_name='Modificado el: ', auto_now_add=False, blank=True,null=True)

	def __unicode__(self):
		return u"de %s %s" % (self.id_responsable.nombre,self.id_responsable.apellido)
	 
	class Meta:
		ordering = ['dia_grupo']
		verbose_name_plural = 'Grupos'


	