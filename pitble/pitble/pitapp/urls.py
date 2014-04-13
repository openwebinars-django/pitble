from django.conf.urls import patterns, url


urlpatterns = patterns('pitble.pitapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^sign-in$', 'signIn', name='signIn'),
    url(r'^followers/$', 'followers', name='followers'),
)
