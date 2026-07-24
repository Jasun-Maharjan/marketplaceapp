from django.contrib import admin
from . models import Category, Product
from django.utils.html import format_html
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','price','stock','status')
    def image_preview(self, obj):
        if obj.project_image:
            return format_html('<img src="{}" width = "80" height = "80" style="object-fit:cover;"/>',obj.product_image.url)
        return "No image"
    image_preview.short_description = "Image"

admin.site.register(Product,productAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Category,CategoryAdmin)

