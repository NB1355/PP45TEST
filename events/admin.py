from django.contrib import admin
from .models import Event, Category

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'description',
        'date',
    )

    ordering = ('date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
