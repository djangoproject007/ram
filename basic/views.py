#django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q


#parent directory
from .forms import UserRegistrationForm

#request is a httprequestobject sent by the user
from posts.models import Post
from userprofile.models import UserProfileData

from functools import reduce
import requests
from bs4 import BeautifulSoup


def index(request):
    if not request.user.is_authenticated():
        return redirect('basic:login')
    posts = Post.objects.filter(user__in=request.user.userprofiledata.following.all()).order_by("-time_created")
    return render(request, 'base/index.html', {
        'posts': posts
    })

def see_about(request):
    return render(request, "base/about.html")


def see_privacy(request):
    return render(request, "base/privacy.html")


def see_terms(request):
    return render(request, "base/terms.html")


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            UserProfileData.objects.create(user=new_user)
            admin = User.objects.get(username="admin")
            new_user.userprofiledata.following.add(admin)
            return HttpResponseRedirect("/signup_success/")
    else:
        form = UserRegistrationForm()
    return render(request, "base/signup.html", {"form": form})



def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('basic:index')

    return render(request, 'base/login.html', {
        'form': form
    })


def signout(request):
    logout(request)
    return render(request, 'base/logged_out.html')


def signup_success(request):
    return render(request, 'base/signup_success.html')


@login_required
def explore(request):
    query = request.GET.get('search')
    if str(query) is '':
        return HttpResponseRedirect('/')
    query = query.split()
    posts_list = Post.objects.filter(user__in=request.user.userprofiledata.following.all())
    search_data = posts_list.filter(reduce(lambda x, y: x | y, [Q(content__icontains=word) | Q(title__icontains=word) for word in query])).order_by("-time_created")
    people = User.objects.filter(reduce(lambda x, y: x | y, [Q(username__icontains=word) | Q(first_name__icontains=word) | Q(email__icontains=word) | Q(last_name__icontains=word) for word in query])).exclude(username="admin")
    request_user_subscriptions = request.user.userprofiledata.following.all()
    context_data = {
        'search_data': search_data,
        'query': query,
        'people': people,
        'request_user_subscriptions' : request_user_subscriptions,
    }
    return render(request, 'base/search.html', context_data)


def circulars(request):
    url = 'http://www.abes.ac.in/about/overview/circulars'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    table = soup.findAll('table')
    return render(request, "base/circulars.html", {"table": table})


def circularredirect(request):
    url = 'http://www.abes.ac.in' + request.get_full_path()
    return redirect(url)

def directory(request):
    if not request.user.is_authenticated():
        return redirect('basic:login')
    profiles = UserProfileData.objects.all()

    context = {
        'header': 'Directory',
        'profiles': profiles,
    }
    return render(request, 'base/directory.html', context)

