from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from testApp.forms import signUpForm


# Create your views here.
def home_view(request):
    return render(request,'testApp/home.html')

@login_required
def foundation_view(request):
    return render(request,'testApp/foundation.html')
@login_required
def intermediate_view(request):
    return render(request,'testApp/intermediate.html')
@login_required
def final_view(request):
    return render(request,'testApp/final.html')
def logout_view(request):
    return render(request,'testApp/logout.html')
def signup_view(request):
    form = signUpForm()
    if request.method == 'POST':
        form = signUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login')
    return render(request,'testApp/signup.html',{'form':form})
