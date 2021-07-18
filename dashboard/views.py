from django.contrib import auth
from django.contrib.messages.api import error
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from dashboard.models import Feedback
from dashboard.models import Book
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
 
from datetime import datetime

# Create your views here.
def XYZ(request):
   return render(request, 'XYZ.html')

def pool(request):
   return render(request, 'pool.html')

def doctor(request):
   return render(request, 'doctor.html')

def spa(request):
   return render(request, 'spa.html')

   
def catering(request):
   return render(request, 'catering.html')

def courier(request):
   return render(request, 'courier.html')

def Drycleaning(request):
   return render(request, 'Drycleaning.html')
   

def Destination(request):
   return render(request, 'Destination.html')

def carrental(request):
   return render(request, 'carrental.html')

def profile(request):
   return render(request, 'profile.html')


@login_required()
def editprofile(request):
       




       if request.method == 'POST':
             
         
         fn = request.POST['fname']
         ln = request.POST['lname']
         em  = request.POST['email']
         un = request.POST['uname']
        

        
              
          

         myuser = User.objects.get(id=request.user.id)
         myuser.first_name= fn
         myuser.last_name= ln
         myuser.username=un
         myuser.email=em
         myuser.save()
         messages.success(request, "your  changes done sucessfully!!!")

        
         return redirect( 'profile')



       else:
        return render(request,'editprofile.html')  
   
@login_required()
def feedback(request):
   if request.method == 'POST':
      # if user !=login:
      #    messages.error(request,"@login_required")
      #    return redirect('home')
   
     
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      name = request.POST.get('name')
      place = request.POST.get('place')
      feedback = Feedback(email=email, phone=phone,  name=name, place=place , date=datetime.today())
      feedback.save()
      messages.success(request, "your feedback submitted")
      # return redirect ('home')
   return render(request, 'feedback.html')
   



def handleSignup(request):
      if request.method == 'POST':
             
         username = request.POST['username']
         fname = request.POST['fname']
         lname = request.POST['lname']
         email  = request.POST['email']
         password1 = request.POST['password1']
         password2 = request.POST['password2']

         # chck erroes
         if  password1 != password2:
            messages.error(request, "passwords doesnt match")   
            return redirect( 'home')

         if not username.isalnum():
            messages.error(request, "username is not alphanumeric")   
            return redirect( 'home')
              
          

         myuser = User.objects.create_user(username, email, password1)
         myuser.first_name= fname
         myuser.last_name= lname
         myuser.save()
         messages.success(request, "your  account has been succesful created")

         # value error comes when redirect is npt taken
         return redirect( 'home')


      else:
        return HttpResponse('404 - noty found')       
        
def handleLogin(request):
   if request.method == 'POST':
             
    loginusername = request.POST['loginusername']
    loginpassword = request.POST['loginpassword']

    user = authenticate(username=loginusername, password=loginpassword)

    if user is not None:
       login(request, user )
       messages.success(request, " loged in sucessful")
       return redirect('home')
    else:
      messages.error(request, " loged in unsucessful please tryagain ")   
      return redirect('home') 
           
    
   return HttpResponse('404-not found')
     
def handleLogout(request):
   
   logout(request)
   messages.success(request, " loged out ")
   return redirect('home')
  

def search(request):
   return redirect ('feedback')
   
          
    

 
     

def book(request):
   if request.method == 'POST':
       
     
      email2 = request.POST.get('email2')
      phone2 = request.POST.get('phone2')
      name2 = request.POST.get('name2')
      place2 = request.POST.get('place2')
      days = request.POST.get('days')
      come = request.POST.get('come')
      end = request.POST.get('end')
      select1=request.POST.get('select1')
      select2=request.POST.get('select2')
      cometime=request.POST.get('cometime')
      endtime=request.POST.get('endtime')
      book = Book(email2=email2, phone2=phone2,  name2=name2, place2=place2, days=days, come=come, end=end,select1=select1,select2=select2, cometime=cometime, endtime=endtime)
      messages.success(request,"booking done sucessfully thankyou")
      book.save()
      
   return render(request, 'book.html')
