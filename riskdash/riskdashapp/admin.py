from django.contrib import admin

from .models import RISK,RISK_TYPE,CONTROLS,RISK_OWNERS,CONTROL_OWNERS,LIKELIHOOD_RATING,RES_LIKELIHOOD_RATING,IMPACT_RATING,CONTROL_STATUS,RISKADMIN,CONTROLSADMIN

admin.site.register(RISK,RISKADMIN)
admin.site.register(RISK_TYPE)
admin.site.register(CONTROLS,CONTROLSADMIN)
admin.site.register(RISK_OWNERS)
admin.site.register(CONTROL_OWNERS)
admin.site.register(LIKELIHOOD_RATING)
admin.site.register(RES_LIKELIHOOD_RATING)
admin.site.register(IMPACT_RATING)
admin.site.register(CONTROL_STATUS)

