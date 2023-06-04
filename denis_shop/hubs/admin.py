from django.contrib import admin
from hubs.models import Categories


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug_category']
    prepopulated_fields = {'slug_category': ('title',)}


admin.site.register(Categories, CategoryAdmin)
