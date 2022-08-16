from django.contrib import admin
from .models import Profile, Contact, Portfolio, Services, Skill

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Services)