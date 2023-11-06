from django import forms
from core.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc', 'image']
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "desc": forms.Textarea(attrs={"class":"form-control"}),
            "image": forms.FileInput(attrs={"class":"form-control"}),
        }
           # labels = {
        #     "name": _("Writer"),
        # }
        # help_texts = {
        #     "name": _("Some useful help text."),
        # }
        # error_messages = {
        #     "name": {
        #         "max_length": _("This writer's name is too long."),
        #     },
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # exclude = ()
        fields = ['desc']
        widgets = {
            "desc": forms.Textarea(attrs={"class":"form-control"}),
        }