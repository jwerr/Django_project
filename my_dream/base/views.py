from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout 
from django.contrib.auth.models import User

from django.contrib import messages
from .forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User




def home(request):
    return render(request, 'base/home.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login  # Rename to avoid conflict
from django.contrib.auth.models import User
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create user but don't save it yet
            user = form.save(commit=False)
            # Set the password
            user.set_password(form.cleaned_data['password'])
            # Save the user
            user.save()
            
            # Log the user in after signup
            auth_login(request, user)  # Use auth_login to avoid conflict
            
            # Redirect to a success page (you can replace this with your desired page)
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'base/signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, 'Please fill in both email and password.')
            return redirect('login')

        # Fetch all users with the provided email
        users = User.objects.filter(email=email)
        
        if users.exists():
            user = users.first()  # Get the first matching user
            
            # Authenticate using the username (user.username) and password
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful! Welcome back.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'No account found with this email.')

    return render(request, 'base/login.html')




def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def about(request):
    return render(request, 'base/about.html')