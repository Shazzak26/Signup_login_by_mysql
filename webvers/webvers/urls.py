
from django.contrib import admin
from django.urls import path
from login.views import *
from signup.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signupact),
    path('login/', loginact),
    
    
]
