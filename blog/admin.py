from django.contrib import admin
from .models import Post, SubscribedUsers

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(SubscribedUsers, SubscribedUsersAdmin)