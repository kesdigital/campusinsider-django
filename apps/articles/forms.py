from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from .models import Article, Tag


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ("tags",)

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tag.objects.all()
