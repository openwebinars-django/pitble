from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from django.contrib.auth import get_user_model


class PitbleUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            get_user_model()._default_manager.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class PitbleUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'
