from django.urls import path 
from . import views 
urlpatterns = [
    path("login-user",views.user_login,name ="login_user"),
    path("logut-user",views.user_logout,name="logout_user"),
    path("user-register",views.user_register,name = "registration"),
    path("create-profile",views.create_profile_page,name ="create_profile_page"),
    path("student-profile/<student_id>",views.user_profile_page,name ="profile_page"),
    
]
