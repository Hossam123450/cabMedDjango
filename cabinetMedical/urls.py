from . import views
from django.urls import path
app_name='cabinetMedical'
urlpatterns = [ path('cab',views.cab,name='cab'),]
