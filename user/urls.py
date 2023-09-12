
from django.urls import path

from user.views import login_view, register_view

urlpatterns = [
    path('', register_view, name='register'),
    path('login', login_view, name='login'),

]
