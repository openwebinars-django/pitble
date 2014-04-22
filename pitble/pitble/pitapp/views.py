from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from pitble.pitapp.forms import SignInForm


def index(request):
    return render_to_response('pitapp/index.html',
                              {},
                              context_instance=RequestContext(request))


def followers(request):
    user = request.user
    return render_to_response('pitapp/followers.html',
                              {'followers': user.followers.all()},
                              context_instance=RequestContext(request))


def sign_in(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    form = SignInForm(data=data)
    if form.is_valid():
        user = form.user
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    return render_to_response('pitapp/sign-in.html',
                              {'form': form,},
                              context_instance=RequestContext(request))