from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .models import Comment


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'status', 'created_on')
	list_filter = ("status",)
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug' : ('title',)}

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'body', 'post', 'created_on', 'active')
	list_filter = ('active', 'created_on')
	search_fields =('name', 'body')
	actions =['approve_comments']

def approve_comments(self, request, queryset):
	queryset.update(active=True)

class PostAdmin(SummernoteModelAdmin):
	summernote_fields = ('content',)
		
admin.site.register(Post,PostAdmin)