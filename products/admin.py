from django.contrib import admin
from . models import Category, Product
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','price','stock','status')

admin.site.register(Product,productAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Category,CategoryAdmin)

