from django.contrib import admin
from .models import BlogPost
# Register your models here.

@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish_date'
    list_display = ('title','slug','author','publish_date','status')
    search_fields = ()
    list_filter = ('author','status','created_date','publish_date')
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}
    search_fields = [ 'author','title' ]
    ordering = ('status', 'publish_date')
    raw_id_fields = ('author',)


