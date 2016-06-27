# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#def index(request):
#    return HttpResponse("Risk Dashboard will appear here")

# Create your views here.

from .models import Risk

def index(request):
    top_risk_list = Risk.objects.order_by('riskref')[:4]
    template = loader.get_template('index.html')
    context = {
        'top_risk_list': top_risk_list,
    }
#    output = ', '.join([q.riskref for q in top_risk_list])
    return HttpResponse(template.render(context, request))
