from django.conf.urls import patterns, url


urlpatterns = patterns('pitble.views',
    url(r'^$', 'index', name='index'),
    url(r'^sign-in/$', 'sign_in', name='sign_in'),
    url(r'^sign-up/$', 'sign_up', name='sign_up'),
    url(r'^sign-out/$', 'sign_out', name='sign_out'),
    url(r'^followers/$', 'followers', name='followers'),
    url(r'^followings/$', 'followings', name='followings'),
    url(r'^create-pitble/$', 'create_pitble', name='create_pitble'),
    url(r'^users/(?P<username>[\w-]+)/$', 'pitbles_by_user', name='pitbles_by_user'),
    url(r'^pitbles/$', 'my_pitbles', name='my_pitbles'),
    url(r'^follow/(?P<username>[\w-]+)$', 'follow_user', name='follow_user'),
)
