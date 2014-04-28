from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from pitble.models import Pitble
from pitble.forms import PitbleUserChangeForm, PitbleUserCreationForm


class PitbleUserAdmin(UserAdmin):
    add_form = PitbleUserCreationForm
    form = PitbleUserChangeForm
    filter_horizontal = UserAdmin.filter_horizontal + ('followings',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Pitble fields'), {'fields': ('followings',)}),
    )


class PitbleAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner')
    search_fields = ('text',)

admin.site.register(get_user_model(), PitbleUserAdmin)
admin.site.register(Pitble, PitbleAdmin)