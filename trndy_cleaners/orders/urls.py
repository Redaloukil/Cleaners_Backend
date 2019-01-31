from django.conf.urls import url
from trndy_cleaners.orders.views import ( 
    OrderDetailView,
    ClientOrderCreate,
)

app_name = "orders"
urlpatterns = [
    url(r'^create/$', ClientOrderCreate.as_view() ),
    
    
    

]
