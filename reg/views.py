from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from reg.forms import UserForm,UserProfileForm
def home(request):
    return render(request,"home.html",{})
def registration(request):
    registered = False;
    if request.method == "POST":
        user_form = UserForm(request.POST)
        user_profile = UserProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=user_profile.save(commit=False)
            profile.user = user
            user_profile.save(commit=True)
            registered = True;
        else:
            print(user_form.errors,user_profile.errors)
    else:
        user_form = UserForm()
        user_profile = UserProfileForm()
    return render(request,"register.html",{'user_form':user_form,'user_profile':user_profile,'registered':registered})
