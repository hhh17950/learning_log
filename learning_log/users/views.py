#coding=gbk
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.models import User
from .forms import RegisterForm,ChangeForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
def register(request):
    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #让用户自动登录，再重新定向到主页
            authenticate_user = authenticate(username = new_user.username,password = request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request,'users/register.html',context)


def change(request):
    if request.method != 'POST':
        form = ChangeForm()
    else:
        form = ChangeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            old_password = form.cleaned_data['old_password']
            new_password_1 = form.cleaned_data['new_password_1']
            new_password_2 = form.cleaned_data['new_password_2']
            user = authenticate(username=username, password=old_password)
            if user:
                if new_password_1 == new_password_2:
                    User.objects.filter(username=username, password=old_password).update(username=username, password=new_password_1)
                    user.set_password(new_password_1)
                    user.save()
                    return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/change.html',context)



