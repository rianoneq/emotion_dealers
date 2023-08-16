from django.contrib import admin
from .models import Product
from .models import Category
from .models import Mark
from .models import PostProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'id': ('name',)}

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    ...

class PostImageAdmin(admin.StackedInline):
    model = PostProductImage  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ['mark', 'price',
                    'category', 'created', 'updated']
    list_filter = ['created', 'updated']
