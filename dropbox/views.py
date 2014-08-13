from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
import json

# Create your views here.

def home(request):
    data = {
        'user': request.user,
    }
    return render(request, "home.html", data)


def check_login(request):
    if request.user.is_authenticated():
        return HttpResponse(json.dumps({'result': {'logged': True}, 'user': request.user}),
                        content_type="application/json")
    else:
        return HttpResponse(json.dumps({'result': {'logged': False}}),
                        content_type="application/json")


"""
USER PROFILES
"""

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("profile")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile(request):
    data = {
        'user': request.user,
    }
    return render(request, 'profile/profile.html', data)


@login_required
def profile_update(request, user_id):
    print request.method
    user = User.objects.get(id=user_id)
    print user_id
    print user
    print user.first_name
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=user)
        print form.is_valid()
        if form.is_valid():
            print '2valid form'
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            print '3valid form'
            return redirect("profile")
    else:
        form = UserChangeForm(instance=user)
    data = {"user": request.user, "form": form}
    return render(request, "profile/profile_update.html", data)

