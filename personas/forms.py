from django import forms
from django.forms import ModelForm
from personas.models import Ficha_Persona,Tipo_Info_Extra
import datetime
from django.forms.extras.widgets import SelectDateWidget
from image_cropping import ImageCropWidget
class ExampleForm(forms.Form):
    username = forms.CharField(max_length=30, label=u'Username')
    email = forms.EmailField(label=u'Email address')
    
class Tipo_ExtraForm(ModelForm):
	class Meta:
		model = Tipo_Info_Extra

class FichaForm(ModelForm):
	
	class Meta:
		model = Ficha_Persona
		fields = ('imagen', 'fecha_nacimiento', 'fecha_miembro')
		widgets = {'imagen': ImageCropWidget,'fecha_nacimiento' :  SelectDateWidget(years=reversed(range(1930, datetime.date.today().year))), 'fecha_miembro': SelectDateWidget(years=reversed(range(1940, datetime.date.today().year))) }