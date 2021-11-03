from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
# models.py에 생성해 놓은 Post 모델을 등록 - > admin 페이지에서 post 보임
admin.site.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)