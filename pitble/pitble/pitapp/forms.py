from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from pitble.pitapp.models import User


class PitbleUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)


class PitbleUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'
