from django.contrib import admin
from .models import Profile, Contact, Portfolio, Services, Skill
from .form import ProfileForm, ContactForm, PortfolioForm, ServicesForm, SkillForm


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
admin.site.register(Profile, ProfileAdmin)

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
admin.site.register(Contact, ContactAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioForm
admin.site.register(Portfolio, PortfolioAdmin)

class ServicesAdmin(admin.ModelAdmin):
    form = ServicesForm
admin.site.register(Services, ServicesAdmin)

class SkillAdmin(admin.ModelAdmin):
    form = SkillForm
admin.site.register(Skill, SkillAdmin)