#encoding=utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
	titulo = 'Index'
	lista = [2,3,5,5,8,5,5,5,5,5,]
	return render_to_response('index.html', context_instance=RequestContext(request))


def hola(request):
	titulo = 'Index'
	lista = [2,3,5,5,8,5,5,5,5,5,]
	return render_to_response('libro/new_libro.html',{'nojodas':titulo,
		'lista':lista}, context_instance=RequestContext(request))


def roger(request):
	return render_to_response('actor/new_actor.html', context_instance=RequestContext(request))