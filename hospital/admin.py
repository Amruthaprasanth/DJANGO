from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(user)
admin.site.register(Book)
admin.site.register(employe)
admin.site.register(Product)
admin.site.register(Customer)
class bok(admin.ModelAdmin):
    list_display=('title','isbn','publi',)
    search_fields=('title',)
    list_filter=('date',)
admin.site.register(bokk,bok)
admin.site.register(publisher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Organizer)
admin.site.register(Event)
