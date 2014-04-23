from django.contrib.auth import get_user_model


def admins(request):
    return {'admins': get_user_model().objects.filter(is_superuser=True)}