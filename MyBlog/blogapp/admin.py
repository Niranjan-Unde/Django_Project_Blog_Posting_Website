from django.contrib import admin
from blogapp.models import Post

# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','sdetail','detail','cat','status','created_on']
    list_filter = ['cat','status']