from django.conf import settings


def i18n(request):
    return {'LANGUAGE_COOKIE_NAME': settings.LANGUAGE_COOKIE_NAME}