# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import operator
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.

from .models import RISK, CONTROLS

def index(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def controls(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    control_list = CONTROLS.objects.order_by('controlref')
    template = loader.get_template('controls.html')
    context = {
        'control_list': control_list,
    }
    return HttpResponse(template.render(context, request))

def risks(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    full_risk_list = sorted(RISK.objects.all(), key=lambda d: (d.resscore,d.absscore), reverse=True)
    template = loader.get_template('details.html')
    context = {
        'full_risk_list': full_risk_list,
    }
    return HttpResponse(template.render(context, request))

def summary(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    top_risk_list = sorted(RISK.objects.all(), key=lambda d: (d.resscore,d.absscore), reverse=True)
    template = loader.get_template('summary.html')
    context = {
        'top_risk_list': top_risk_list,
    }
    return HttpResponse(template.render(context, request))

def topten(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    top_risk_list = sorted(RISK.objects.all(), key=lambda d: (d.resscore,d.absscore), reverse=True)[:10]
    template = loader.get_template('summary.html')
    context = {
        'top_risk_list': top_risk_list,
    }
    return HttpResponse(template.render(context, request))

