from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from app import programa_controller

def index(request) :
    return render_to_response('layout.html')

def translate(request) :
	word 	 = request.GET.get('word')
	language = request.GET.get('language')

	prC = programa_controller.Programa()
	wordsTranslate = prC.getTranslate(language, word)
	return JsonResponse(wordsTranslate, safe=False)