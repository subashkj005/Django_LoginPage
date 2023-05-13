from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache

# Create your views here.


@never_cache
def HomePage(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    else:
        return redirect('login')


@never_cache
def LoginPage(request):
    if 'username' in request.session:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['username'] = username
                return redirect('home')
            else:
                message = "Username or Password is incorrect"
                return render(request, 'login.html', {'message': message})
        return render(request, 'login.html')


@never_cache
def LogoutPage(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')
