from django.contrib import admin
from sheets.models import Cheatsheets, CheetsheetComment

# Register your models here.

admin.site.register(CheetsheetComment)

@admin.register(Cheatsheets)
class BlogsAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/tinyInject.js",)
