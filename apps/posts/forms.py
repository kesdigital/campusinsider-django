from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from .models import Post, Tag


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("tags",)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()
