from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout

# Create your views here.


def accounts_handler(request):
    

    login_form=AuthenticationForm()
    signup_form =UserCreationForm()
    for _ in signup_form.fields:
        signup_form.fields[_].help_text=None

    context={"login_form":login_form,
             "signup_form":signup_form}
    
    return render(request,"accounts/base.html",context=context)


def login_handler(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("blog")
        else:
            return redirect('accounts')
    
    else:
        return HttpResponseNotAllowed('POST')
def signup_handler(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            print('valid')
            user=form.save()
            login(request,user)
            return redirect('blog')
        else:
            return redirect('accounts')
    else:
        return HttpResponseNotAllowed('POST')


def logout_handler(request):
    if request.method=="POST":
        logout(request)
        return redirect("accounts")