from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from blog.models import Blogs
from sheets.models import Cheatsheets
from django.core.paginator import Paginator

# Create your views here.

def sheets(request):
    allPosts = Cheatsheets.objects.all().order_by('sno')
    paginator = Paginator(allPosts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj" : page_obj}
    return render(request, 'home/sheets.html', context)


def blogspage(request):
    allPosts = Blogs.objects.all().order_by('sno')
    paginator = Paginator(allPosts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj" : page_obj}
    return render(request, 'home/blog.html', context)


def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def signup(request):
    return render(request, 'home/signup.html')

def login(request):
    return render(request, 'home/login.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, country=country, description=description, date=datetime.today())
        contact.save()


    return render(request, 'home/contact.html')
    
def search(request):
    query = request.GET['query']
    if len(query)>70:
        allPosts = Cheatsheets.objects.none()
    else:
        allPostsTitle = Cheatsheets.objects.filter(title__icontains=query)
        allPostsContent = Cheatsheets.objects.filter(subtitle__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    params = {"allPosts": allPosts, "query": query}
    return render(request, "home/search.html", params)

def handleSignup(request):
    if request.method =="POST":
    # Get the post parameters
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]    


        # Create the user

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect("/login")


    else:
        return HttpResponse("404 not found")

def handleLogin(request):

    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth_login(request, user)
            return redirect("/")

        else:
            messages.error(request, 'Login Credentials did not match')
            return redirect('/login') 
        
    return HttpResponse("404 - NOT FOUND")
def handleLogout(request):
    logout(request)
    return redirect("/")


