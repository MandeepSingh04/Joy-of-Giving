from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import *

# superuser
# username - man
# password - man

def index(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def mypost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mypost.html', {'post': post})
    
def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been submitted successfully")
            return render(request, 'post.html', {'form' : form})
    else:
        form = PostForm()
    return render(request, 'post.html', {'form' : form})

def userlogin(request):
    return render(request, 'login.html')

def usersignup(request):
    return render(request, 'signup.html')

def handlesignup(request):
    if request.method == 'POST':
        #post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        #check for incorrect inputs

        if len(username)>20:
            messages.error(request, "Username cannot exceed 20 characters")
            return redirect('usersignup')

        if not username.isalnum():
            messages.error(request, "Username must contain only letters and numbers")
            return redirect('usersignup')

        if password!=confirm_password:
            messages.error(request, "Incorrect password")
            return redirect('usersignup')

        #create user
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "You have successfully created your account!")
        return redirect('home')
    else:
        return HttpResponse("404 not found")

def handlelogin(request):
    if request.method == 'POST':
        lusername = request.POST['loginusername']
        lpassword = request.POST['loginpassword']

        user = authenticate(username=lusername, password=lpassword)

        if user is not None:
            login(request, user)
            messages.success(request,"You have succesfully logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials, please try again!")
            return redirect('userlogin')

def handlelogout(request):
    logout(request)
    messages.success(request, "You have been successfully Logged out!")
    return redirect('home')