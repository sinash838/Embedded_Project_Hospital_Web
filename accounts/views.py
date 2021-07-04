from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('patients:beds_list'))


def login_user(request):
    """ redirecting to home if authenticated """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('patients:beds_list'))
    """ logging in """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('patients:beds_list'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'accounts/login.html', {})


@login_required
def logout_user(request):
    logout(request)
    return render(request, 'accounts/login.html', {})
