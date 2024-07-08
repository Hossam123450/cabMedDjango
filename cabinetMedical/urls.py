from . import views
from django.urls import path
app_name='cabinetMedical'
urlpatterns = [
               path('cab/',views.cab,name='cab'), 
               path('cab1/',views.cab1,name='cab1'),
               path('cab2/',views.cab2,name='cab2'),
               path('cab3/',views.cab3,name='cab3'),
               path('cab4/',views.cab4,name='cab4')
            
            ]
               

