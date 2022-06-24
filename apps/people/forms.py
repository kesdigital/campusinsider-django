from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from .models import Profile, Role


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("roles",)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["roles"].widget = CheckboxSelectMultiple()
        self.fields["roles"].queryset = Role.objects.all()
