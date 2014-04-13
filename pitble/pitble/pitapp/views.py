from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms

# Create your views here.
def index(request):
    return render_to_response('pitapp/index.html',
                              {},
                              context_instance=RequestContext(request))

def followers(request):
    user = request.user
    return render_to_response('pitapp/followers.html',
                              {'followers': user.followers.all()},
                              context_instance=RequestContext(request))
    
class signInForm(forms.Form):
    email = forms.CharField(max_length=100, required=True)
    password = forms.PasswordInput()
    
def signIn(request):
    if request.method == 'POST': 
        form = signInForm(request.POST) 
        if form.is_valid():
            # LLamar al modelo para verificar si el usuario existe
            pass 
    else:
        form = signInForm()
        
    return render_to_response('pitapp/sign-in.html',
                              {'form': form,},
                              context_instance=RequestContext(request))