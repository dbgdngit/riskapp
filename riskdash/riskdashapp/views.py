# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import operator

# Create your views here.

from .models import Risk

def index(request):
#    top_risk_list = Risk.objects.order_by('riskref')[:10]
    top_risk_list = sorted(Risk.objects.all(), key=lambda d: d.Score, reverse=True)[:10]
    template = loader.get_template('index.html')
    context = {
        'top_risk_list': top_risk_list,
    }
    return HttpResponse(template.render(context, request))

def controls(request):
    return HttpResponse('Control view to be completed')

def risks(request):
    return HttpResponse('Risk detailed view to be completed')

def summary(request):
    return HttpResponse('Summary view to be completed')

def topten(request):
    return HttpResponse('Top Ten view to be completed')

