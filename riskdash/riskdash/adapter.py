from django.http import HttpResponse

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user   
        if not u.email.split('@')[1] == "guardian.co.uk":
           raise ImmediateHttpResponse(HttpResponse('You are not an approved user'))
