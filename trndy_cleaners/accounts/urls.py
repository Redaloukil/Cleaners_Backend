from django.conf.urls import url
from trndy_cleaners.accounts.views import (
    ClientDetailView ,
    EmployeeDetailView , 
    ClientListView , 
    EmployeeListView
)


app_name = "accounts"

urlpatterns = [
    url(r'^clients/$', ClientListView.as_view()),
    url(r'^clients/(?P<user_id>[\d]+)$', ClientDetailView.as_view()),
    url(r'^employees/$', EmployeeListView.as_view()),
    url(r'^employees/(?P<user_id>[\d]+)$', EmployeeDetailView.as_view()),
]