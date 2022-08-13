from django.contrib import admin
from .models import Post, Comment, Categorie

admin.site.register(Categorie)
admin.site.register(Post)
admin.site.register(Comment)

