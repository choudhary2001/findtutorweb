
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('studentsignup/',views.studentsignup,name='studentsignup'),
    path('search/',views.search,name='search'),
    path('studetails/<int:pk>',views.studetails,name='studetails'),
    path('tutordetails/<int:pk>',views.tutordetails,name='tutordetails'),
    # path('tutorsearch/',views.tutorsearch,name='tutorsearch'),
    path('tutorsignup/',views.tutorsignup,name='tutorsignup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
]
# studetails