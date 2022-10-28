from django.contrib import admin
from .models import Category, Product, Book, BookItem, DeliveryAddress, Refund


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['available', 'company', 'country']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(DeliveryAddress)
admin.site.register(Refund)



