from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DetailView

from user.models import User
# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:     
                login(request, user)              
                return redirect('home')               
            else:
                messages.error(request, "Vous etez pas encore client")
                return render(request, 'user/login.html', {})
        else:
            return render(request, 'user/login.html', {})
    else:
        return redirect('register')

# def register_view(request):
#     if request.method == 'POST':
#         # Get user input from the registration form

#         first_name = request.POST['first_name']
#         print(first_name)
#         last_name = request.POST['last_name']
#         print(last_name)
#         password = request.POST['password']
#         email = request.POST['email']

#         # Create a new user using the User model
#         user = User.create_user( first_name=first_name, last_name=last_name,  password=password, email=email)

#         # Log the user in
#         login(request, user)

#         # Redirect to a success page or wherever you want
#         return redirect('login')  # Replace 'success_page' with your desired URL

#     return render(request, 'user/register.html')  # Create a registration template





def register_view(request): 
    if request.method == "POST":
        first_name = request.POST['first_name']
        print(first_name)
        last_name = request.POST['last_name']
        print(last_name)
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
        user = User.objects.create_user( first_name=first_name, last_name=last_name, email=email,
          password=password)
        print(user)
  
        print('Valideeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')      
        return redirect('login')
   
    else:
        print('non validesssssssssssssssssssssssssssssssssssssssssssssssssss')
        return render(request, 'user/register.html', )