from django.contrib import admin
from .models import Author,Post,Tag,Comment

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug", )
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("tags","author","date")
    list_display = ("title","author","date")
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "post")
    
admin.site.register(Author)
admin.site.register(Post,PostAdmin) #if you didn't pass postAdmin with post it will not work
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)



