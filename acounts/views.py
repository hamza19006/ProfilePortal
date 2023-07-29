from django.contrib.auth import login
from django.contrib.auth.models import User , auth
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm-password']

        user = User.objects.create_user(username = username , email = email , password = password1)
        user.save()
        return redirect('/')
    else:
        return render(request, 'register.html')
    


def login(request) :
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request , user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error':'invalid username or password'})
    else:
        return render(request, 'login.html')




def logout(request):
    auth.logout(request)
    return redirect('/')