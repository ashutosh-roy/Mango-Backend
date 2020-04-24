from users.views import RegistrationAPI,LoginAPI
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]
