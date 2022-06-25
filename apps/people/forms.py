from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from .models import Profile, Role


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("other_roles",)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["other_roles"].widget = CheckboxSelectMultiple()
        self.fields["other_roles"].queryset = Role.objects.all()
