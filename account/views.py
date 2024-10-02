from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(request,username=form_data['username'],password=form_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('product:product_list')
            else:
                return HttpResponse('invalid login')
        
    form = LoginForm()
    return render(request,'account/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('account:login')