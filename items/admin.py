from django.contrib import admin
from .models import Item, Tag, SearchLog

# Register your models here.
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(SearchLog)
