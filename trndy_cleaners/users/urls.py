from django.conf.urls import url
from trndy_cleaners.users.views import ( 
    SignupView,
    LoginView , 
    LogoutView , 
    ResetPasswordView , 
    UpdatePasswordView , 
    UserView , 
    UserDetail ,
   
    
)
app_name = "users"

urlpatterns = [
    # Login / logout
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^signup/$', SignupView.as_view()),

    # Password management
    url(r'^reset_password/$', ResetPasswordView.as_view()),
    url(r'^update_password/$', UpdatePasswordView.as_view()),

  

    # Users
    url(r'^users/$', UserView.as_view()),
    url(r'^users/(?P<id>[\d]+)/$', UserDetail.as_view()),
    
]
