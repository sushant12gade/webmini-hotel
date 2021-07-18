from django.urls import path
from django.contrib import admin
from.import views

#  django admin header customization
admin.site.site_header = "login to  devloper XYZ𝓗𝓞𝓣𝓔𝓛𝓢"
admin.site.site_title = "login to   XYZ𝓗𝓞𝓣𝓔𝓛𝓢 dashboard "
admin.site.index_title = "welcome to portal "

urlpatterns = [

 path('',views.XYZ, name='home'),
 path('feedback',views.feedback, name='feedback'),
 path('search',views.search, name='search'),
 path('Destination',views.Destination, name='Destination'),
 path('carrental',views.carrental, name='carrental'),
 path('catering',views.catering, name='catering'),
 path('Drycleaning',views.Drycleaning, name='Drycleaning'),
 path('courier',views.courier, name='courier'),
 path('doctor',views.doctor, name='doctor'),
 path('spa',views.spa, name='spa'),
 path('pool',views.pool, name='pool'),
 path('signup',views.handleSignup, name='handleSignup'),
 path('login',views.handleLogin, name='handleLogin'),
 path('logout',views.handleLogout, name='handleLogout'),
 path('book',views.book, name='book'),
 path('profile',views.profile, name='profile'),
 path('editprofile',views.editprofile, name='editprofile')
]
