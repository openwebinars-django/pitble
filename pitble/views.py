from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from pitble.forms import SignInForm, SignUpForm


def index(request):
    return render_to_response('pitble/index.html',
                              {},
                              context_instance=RequestContext(request))


@login_required
def followers(request):
    user = request.user
    followers = user.followers.all()
    return render_to_response('pitble/followers.html',
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
    return render_to_response('pitble/sign-in.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def sign_up(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    form = SignUpForm(data=data)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.add_message(request, messages.INFO, _('Success create account %s' % user.username))
        return HttpResponseRedirect(reverse('index'))
    return render_to_response('pitble/sign-up.html',
                              {'form': form},
                              context_instance=RequestContext(request))


@login_required
def sign_out(request):
    user = request.user
    logout(request)
    messages.add_message(request, messages.INFO, _('Goodbye %s' % user.username))
    return HttpResponseRedirect(reverse('index'))