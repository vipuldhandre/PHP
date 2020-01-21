from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Attribute
# Register your models here.
class AttributeAdmin(admin.ModelAdmin):
    list_display=['id','title','description']
admin.site.register(Attribute,AttributeAdmin)
