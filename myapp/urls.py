from django.urls import path
from .views import post_list, admin_view
urlpatterns = [    
    path('', post_list, name='post_list'),
    path('admin/', admin_view, name='admin_view'),
]