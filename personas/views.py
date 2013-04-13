from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.core.context_processors import csrf
from django.template import RequestContext
from forms import FichaForm,ExampleForm,Tipo_ExtraForm
from models import Ficha_Persona,Tipo_Info_Extra
from django.db import models,connection
from django_tables2   import RequestConfig
from personas.tables  import PersonaTable
from django.utils import simplejson
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
def render_to_json(*args, **kwargs):
    response = HttpResponse(*args, **kwargs)
    response['mimetype'] = "text/javascript"
    response['Pragma'] = "no cache"
    response['Cache-Control'] = "no-cache, must-revalidate"
    return response

def index(request):
	errores = ''
	if request.is_ajax() and request.method == 'POST':
		form = FichaForm(request.POST)	
		if form.is_valid():
			form.save()
			success = True
		else:
			success = False
			errores = form.errors
			return render_to_json(simplejson.dumps({'errores':errores, 'success': success}))

	else:
		formulario = FichaForm()
		return render_to_response('ejemplo_ajax.html', {'formulario':formulario}, context_instance=RequestContext(request))

@csrf_protect
def autocomplete(request):
	if request.is_ajax() and request.method == 'GET':
		envio = request.GET['search']
		success = True
		datos = Ficha_Persona.objects.extra(where=["CONCAT(nombre,' ', apellido) LIKE %s"], params=["%"+envio+"%"])
		#datos = Ficha_Persona.objects.raw('''SELECT id,nombre,apellidoFROM personas_ficha_personaWHERE nombre = 'Edgardo'''')
		#data = serializers.serialize('json',[{'nombre': p.nombre} for p in datos],fields=('nombre','apellido'))
		return render_to_json(simplejson.dumps({'datos':[{'nombre': p.nombre+ ' ' + p.apellido} for p in datos],'envio':envio, 'success': success}))

	return render_to_response('autocomplete.html', {}, context_instance=RequestContext(request))

def tablas(request):
	if request.is_ajax() and request.method == 'GET':
		table = PersonaTable(Ficha_Persona.objects.all())
		RequestConfig(request).configure(table)
		table.paginate(page=request.GET.get('page', 2), per_page=4)
		success = True
		return render_to_json(simplejson.dumps({'success': success, 'table':[{'nombre': p.nombre} for p in table]}))
	else:
	    table = PersonaTable(Ficha_Persona.objects.all())
	    RequestConfig(request).configure(table)
	    table.paginate(page=request.GET.get('page', 1), per_page=4)
	    return render(request, 'tutorial_tablas.html', {'table': table})

def persona_add(request):
	if request.method == 'POST':
		formulario = FichaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/ficha/')
	else:
		formulario = FichaForm()
	return render_to_response('persona_view.html', {'formulario':formulario}, context_instance=RequestContext(request))

def persona_edit(request, id):
	if request.method == 'POST':
		form = FichaPersonaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ficha/')
	else:
		obj = FichaPersona.objects.get(pk=id)
		form = FichaPersonaForm(instance=obj)
	return render_to_response('persona_view.html', {'form':form}, context_instance=RequestContext(request))
