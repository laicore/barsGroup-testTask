from django.contrib import admin

# Register your models here.
from .models import *


class PlanetModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SithModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'learnPlanet')


class TestTaskModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')

class RecriutInfoAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','planet','handOfShadow')
class UniqueOrdenNumberModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'uniqueTestNumber')


admin.site.register(PlanetModel, PlanetModelAdmin)
admin.site.register(SithModel, SithModelAdmin)
admin.site.register(TestTask, TestTaskModelAdmin)
admin.site.register(UniqueOrdenNumberModel, UniqueOrdenNumberModelAdmin)
admin.site.register(RecruitModel,RecriutInfoAdmin)
