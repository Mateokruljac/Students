from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from events.models import Event, Student
from django.contrib.auth import login,logout,authenticate

from members.forms import ProfilePage
# Create your views here.

def user_register (request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password =  request.POST["password"]
        confirm_password =  request.POST["confirm_password"]
        
        if User.objects.filter(username = username).exists() == False  and User.objects.filter(email = email).exists() == False:
            if password == confirm_password: 
                if email.endswith("fer.unizg"):
                    user = User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        password =  password,
                        email = email
                    )
                    user.save()
                    messages.info(request,"Account successfully created!")
                    return redirect("login_user")
                else:
                    messages.info(request,"You are not FER student!")
                    return render (request,"members/register.html")
            else:
                messages.info(request,"Password not matching!")
                return render (request,"members/register.html")
                
        else:
            messages.info(request,"User with that username or email already exist! Please, use a new username or email!")
            return render (request,"members/register.html")
    
    else:
        return render (request,"members/register.html")
    
    
def user_login(request):
    if request.method == "POST":
        events = Event.objects.all().order_by("event_date") 
        username = request.POST["username"]
        password = request.POST["password"]
        
        #check user`s authentication
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            # return render (request,"events/all_events.html",{"events":events})
            try:
              if request.user.id != request.user.student.student_user.id:
                return redirect("create_profile_page")          
              else:
                   return render (request,"events/all_events.html",{"events":events})
            except: 
                return redirect("create_profile_page") 
        else: 
           messages.info (request,"Invalid username or password. Please try again or use another account!")
           return render (request,"members/login.html")
            
    else:
        return render (request,"members/login.html")

def user_logout(request):
    events = Event.objects.all()
    logout(request)
    return render (request,"events/all_events.html",{"events":events})
    

def create_profile_page(request):
    successfully = False
    if request.method == "POST":
        form = ProfilePage(request.POST,request.FILES)
        if form.is_valid():
           event = form.save(commit = False)             
           event.student_user = request.user
           event.save()
           form.save_m2m()
               
           return HttpResponseRedirect("/members/create-profile?successfully=True")
        #    return render (request,"events/all_events.html",{"events":events})
    else: 
        form = ProfilePage()
        if "successfully" in request.GET:
            successfully = True
        return render(request,"members/create_profile_page.html",{"form":form,"successfully":successfully})
    
def user_profile_page (request,student_id):
    student  = Student.objects.get(pk = request.user.student.id)
    
    #display events user have booked
    events = Event.objects.filter(event_booking = request.user.student.student_user.id)
    
    return render(request,"members/student_page.html",{"student":student,"events":events})
        
        
