from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
    
class RISK_TYPE(models.Model):
    description = models.CharField(max_length=15)

    def __unicode__(self):
        return self.description

class CONTROL_OWNERS(models.Model):
    name = models.CharField(max_length=30,default='')

    def __unicode__(self):
        return unicode(self.name)

class CONTROL_STATUS(models.Model):
    label = models.CharField(max_length=12,default='')

    def __unicode__(self):
        return unicode(self.label)

class CONTROLS(models.Model):
    controlref = models.CharField(max_length=9)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(CONTROL_OWNERS)
    type_of_control = models.CharField(max_length=60)
    status = models.ForeignKey(CONTROL_STATUS)
    is_pci = models.BooleanField(default='False')
    is_cyber_essentials = models.BooleanField(default='False')
    is_iso27001 = models.BooleanField(default='False')
    is_gdpr = models.BooleanField(default='False')

    def __unicode__(self):
        return self.description

class RISK_OWNERS(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.name)


class LIKELIHOOD_RATING(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField(default='0')

    def __unicode__(self):
        return self.label

class IMPACT_RATING(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField(default='0')

    def __unicode__(self):
        return self.label

class RES_LIKELIHOOD_RATING(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField(default='0')

    def __unicode__(self):
        return self.label

class RISK(models.Model):
    riskref = models.CharField(max_length=9)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey("RISK_OWNERS", on_delete=models.CASCADE)
    type_of_risk = models.ManyToManyField("RISK_TYPE")
    created_date = models.DateTimeField('created on')
    last_updated_date = models.DateTimeField('last updated on')
    previous_updated_date = models.DateTimeField('previous update')
    absscore = models.IntegerField(null=True)
    resscore = models.IntegerField(null=True)
    previous_score = models.IntegerField(default='0')
    ranking = models.IntegerField
    previous_ranking = models.IntegerField
    absolute_likelihood = models.ForeignKey("LIKELIHOOD_RATING", on_delete=models.CASCADE)
    absolute_impact = models.ForeignKey("IMPACT_RATING", on_delete=models.CASCADE)
    rating_rationale = models.CharField(max_length=60)
    residual_likelihood = models.ForeignKey("RES_LIKELIHOOD_RATING", on_delete=models.CASCADE)
    associated_controls = models.ManyToManyField("CONTROLS")

    def __unicode__(self):
        return unicode(self.description)

    @property
    def absscore(self):
        return self.absolute_impact.value * self.absolute_likelihood.value

    @property
    def resscore(self):
        return self.absolute_impact.value * self.residual_likelihood.value

class RISKADMIN(admin.ModelAdmin):     
    readonly_fields = ('absscore','resscore',)
    ordering = ('riskref','residual_likelihood','absolute_likelihood','absolute_impact')
    list_display = ('riskref','description','absscore','absolute_impact','absolute_likelihood','resscore','residual_likelihood','owner')

class CONTROLSADMIN(admin.ModelAdmin):     
    ordering = ('description','controlref','status')
    list_display = ('description','controlref','status','owner')
