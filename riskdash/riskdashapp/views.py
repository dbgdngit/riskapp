# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import operator

# Create your views here.

from .models import Risk, Controls

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def controls(request):
    control_list = Controls.objects.order_by('controlref')
    template = loader.get_template('controls.html')
    context = {
        'control_list': control_list,
    }
    return HttpResponse(template.render(context, request))

def risks(request):
    full_risk_list = sorted(Risk.objects.all(), key=lambda d: (d.ResScore,d.AbsScore), reverse=True)
    template = loader.get_template('details.html')
    context = {
        'full_risk_list': full_risk_list,
    }
    return HttpResponse(template.render(context, request))

def summary(request):
    top_risk_list = sorted(Risk.objects.all(), key=lambda d: (d.ResScore,d.AbsScore), reverse=True)
    template = loader.get_template('summary.html')
    context = {
        'top_risk_list': top_risk_list,
    }
    return HttpResponse(template.render(context, request))

def topten(request):
    top_risk_list = sorted(Risk.objects.all(), key=lambda d: (d.ResScore,d.AbsScore), reverse=True)[:10]
    template = loader.get_template('summary.html')
    context = {
        'top_risk_list': top_risk_list,
    }
    return HttpResponse(template.render(context, request))

