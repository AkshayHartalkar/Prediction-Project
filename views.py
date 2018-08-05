from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .models import UserFeedback
from django.http import HttpResponse
from . import forms
# Create your views here.
def loginpage(request):
    if request.method=='POST':
        print(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('HomeApp:home')
        else:
            # formerrors=form.errors
            # print(form.errors.as_data())
            # print(form.errors.get('__all__'))
            return render(request,'loginpage/index.html',{'formerrors':form.errors.get('__all__')})
    else:
        form= AuthenticationForm()
        return render(request,'loginpage/index.html')

def logout_view(request):
    logout(request)
    return redirect('LoginApp:login')

def feedback_view(request):
    if request.method=='POST':
        print(request.POST)
        form = forms.UserFeedback(request.POST)
        if form.is_valid():
            instance=form.save()
            return redirect('LoginApp:login')
        else:
            return HttpResponse(form.errors)
    else:
        return redirect('LoginApp:login')
