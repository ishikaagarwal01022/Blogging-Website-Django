from django.contrib import admin
from blog.models import Blogs, BlogComment


# Register your models here.


admin.site.register(BlogComment)

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/tinyInject.js",)


