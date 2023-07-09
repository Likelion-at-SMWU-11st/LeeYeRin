from django.contrib import admin
from .models import Post
from .models import Question
from .models import Comment

admin.site.register(Question)
admin.site.register(Comment)

class CommentInline(admin.TabularInline): #StackedInline
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'content', 'created_at', 'view_count', 'writer']
    #list_editable = ['content', 'writer']
    list_filter = ['created_at']
    search_fields = ['id', 'writer_username']
    search_help_text = '게시판번호, 작성자 검색이 가능합니다'
    readonly_fields = ['view_count', 'created_at']
    inlines = [CommentInline,]

    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content = '운영규칙 위반으로 인한 게시글 삭제 처리'
            item.save()