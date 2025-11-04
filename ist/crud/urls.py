from django.urls import include, path
from . import views

urlpatterns = [
    path('CREATE/', views.CreateView, name="create"),
    path('show/', views.ShowView, name='list'),
    path('up/<int:f_Sid>/', views.updateView, name= 'update_url'), 
    path('del/<int:f_Sid>/', views.deleteView, name='delete' ),
]
