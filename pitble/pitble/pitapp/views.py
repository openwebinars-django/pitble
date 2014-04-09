from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def index(request):
    return render_to_response('pitapp/index.html',
                              {},
                              context_instance=RequestContext(request))


# Create your views here.
def followers(request):
    return render_to_response('pitapp/followers.html',
                              {},
                              context_instance=RequestContext(request))