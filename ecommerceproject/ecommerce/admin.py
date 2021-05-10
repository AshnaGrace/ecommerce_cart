from django.contrib import admin

# Register your models here.
from ecommerce.models import category, product


class categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields ={
        'slug':('name',)
    }


class productAdmin(admin.ModelAdmin):
    list_display = ['name','slug','desc','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(category,categoryAdmin)
admin.site.register(product,productAdmin)
