from django.contrib import admin
from .models import Document, Post,form,Comment, blogcomment


# Register your models here.
admin.site.register(Post)
admin.site.register(Document)
admin.site.register(form)
admin.site.register(Comment)
admin.site.register(blogcomment)


