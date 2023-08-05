from django.contrib import admin
from.models import category,product

class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryadmin)
class productadmin(admin.ModelAdmin):
    list_display = ['name','slug','created','available','stock','price']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,productadmin)


# Register your models here.
