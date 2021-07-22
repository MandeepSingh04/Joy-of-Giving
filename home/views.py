from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
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

def profile(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request, 'profile.html',context)

def userprofile(request,pk):
    allposts = Post.objects.all()
    User = get_user_model()
    postuser = get_object_or_404(User, pk=pk)
    if request.user==postuser:
        return redirect('profile')
    context = {'allposts':allposts,'postuser':postuser}
    return render(request, 'userprofile.html',context)

def about(request):
    return render(request, 'about.html')

def mypost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    User = get_user_model()
    allusers = User.objects.all()
    context = {'allusers':allusers,'post': post}
    return render(request, 'mypost.html', context)
    
def createpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
    
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, "Your post has been submitted successfully")
                next = request.GET.get('next', reverse('home'))
                return redirect(next)
        else:
            form = PostForm()
        return render(request, 'post.html', {'form' : form})
    else:
        return redirect('login')

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user != post.user:
        next = request.GET.get('next', reverse('mypost',kwargs={'pk': pk}))
        return redirect(next)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been edited")
            next = request.GET.get('next', reverse('mypost', kwargs={'pk': pk}))
            return redirect(next)
        else:
            form = PostForm(instance=post)
    else:
        form = PostForm(instance=post)
    return render(request, 'editpost.html', {'form':form, 'post':post})

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

def deletepost(request,id):
    post_to_delete=Post.objects.get(id=id)
    post_to_delete.delete()
    messages.success(request, "Your post has been deleted successfully!")
    return redirect('home')