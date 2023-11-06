from django.contrib import admin
from core.models import Profile,Post,Comment,Image
from admin_confirm import AdminConfirmMixin
from image_uploader_widget.widgets import ImageUploaderWidget
from django.db import models



class CommentInline(admin.TabularInline):
    model = Comment

class ImageInline(admin.TabularInline):
    model = Image
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }
@admin.register(Post)
class PostAdmin(AdminConfirmMixin,admin.ModelAdmin):
    confirm_change = True
    confirmation_fields = ['title', 'desc']
    list_display = ('id','title', 'desc','author')
    search_fields = ('title','author__username')
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }
    fieldsets = [
        (
            "Post Data",
            {
                "fields": ["author",("title","desc")],
            },
        ),
        (
            "Post Media",
            {
                "classes": ["collapse",],
                "fields": ["image"],
            },
        ),
    ]

    inlines = [CommentInline,ImageInline]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','post','author','desc','is_hidden']
    search_fields = ('id','author__username')
    # list_per_page = 2
    # list_editable = ('post','author','desc')
    def hide_comments(modeladmin, request, queryset):
        queryset.update(is_hidden=True)
    hide_comments.short_description="Hide the Selected Comments"
    def unhide_comments(modeladmin, request, queryset):
        queryset.update(is_hidden=False)
    unhide_comments.short_description="Unhide the Selected Comments"

    actions =[hide_comments,unhide_comments]


admin.site.register(Profile)
