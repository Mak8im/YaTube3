import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

from helloApp.models import Post, Person


def main(request):
    return HttpResponse("main")
def groups(request):
    return HttpResponse("groups")
def lenta(request):
    return render(request,"lenta.html")

def lenta_json(request):
    qs_json = serializers.serialize('json', Post.objects.all())
    return HttpResponse(qs_json, content_type='application/json')
