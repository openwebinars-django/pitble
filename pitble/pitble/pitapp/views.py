from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from pitble.pitapp.forms import SignInForm


def index(request):
    return render_to_response('pitapp/index.html',
                              {},
                              context_instance=RequestContext(request))


@login_required
def followers(request):
    user = request.user
    followers = user.followers.all()
    return render_to_response('pitapp/followers.html',
                              {'followers': followers},
                              context_instance=RequestContext(request))


@login_required
def followings(request):
    raise NotImplementedError


@login_required
def create_pitble(request):
    raise NotImplementedError


@login_required
def my_pitbles(request):
    return pitbles_by_user(request.user)


def pitbles_by_user(request, username):
    raise NotImplementedError


@login_required
def follow_user(request, username):
    raise NotImplementedError


def sign_in(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    form = SignInForm(data=data)
    if form.is_valid():
        user = form.user
        login(request, user)
        messages.add_message(request, messages.INFO, _('Welcome %s' % user.username))
        return HttpResponseRedirect(reverse('index'))
    return render_to_response('pitapp/sign-in.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def sign_up(request):
    raise NotImplementedError