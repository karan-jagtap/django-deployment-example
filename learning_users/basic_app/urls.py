from basic_app import views
from django.conf.urls import url, include

app_name = 'basic_app'

urlpatterns = [
    url('register/', views.register, name="register"),
]
