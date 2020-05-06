from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from userprofile.models import UserProfileData
from .forms import EditInfo
from django.contrib.auth.decorators import login_required
from annoying.decorators import ajax_request
#Returns JsonResponse with dict as content.


def followers(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfileData.objects.get(user=user)
    profiles = user_profile.followers.all

    context = {
        'header': 'Followers',
        'profiles': profiles,
    }

    return render(request, 'profile/follow_list.html', context)


def following(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfileData.objects.get(user=user)
    profiles = user_profile.following.all

    context = {
        'header': 'Following',
        'profiles': profiles
    }
    return render(request, 'profile/follow_list.html', context)


def profile(request, user_username=None):
    user = get_object_or_404(User, username=user_username)
    profile = UserProfileData.objects.get(user=user)
    context = {
        'username': user_username,
        'user': user,
        'profile': profile
    }
    return render(request, 'profile/profile.html', context)


@login_required
def edit_info(request):
    user_profile_data = UserProfileData.objects.get(user=request.user)
    form = EditInfo(request.POST or None, request.FILES or None, instance=user_profile_data)
    if form.is_valid():
        info = form.save(commit=False)
        info.save()
        return redirect('basic:index')
    return render(request, "profile/edit_info.html", {"form": form})


@ajax_request
@login_required
def follow_toggle(request):
    user_profile = UserProfileData.objects.get(user=request.user)
    follow_profile_pk = request.POST.get('follow_profile_pk')
    follow_profile = UserProfileData.objects.get(pk=follow_profile_pk)

    try:
        if user_profile != follow_profile:
            if request.POST.get('type') == 'follow':
                user_profile.following.add(follow_profile.user)
                follow_profile.followers.add(user_profile.user)
            elif request.POST.get('type') == 'unfollow':
                user_profile.following.remove(follow_profile.user)
                follow_profile.followers.remove(user_profile.user)
            user_profile.save()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_profile_pk': follow_profile_pk
    }
