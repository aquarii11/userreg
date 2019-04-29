from django.conf.urls import url
from reg import views
app_name="reg"
urlpatterns = [
    url("^$",views.home,name="home"),
    url("^register$",views.registration,name="register")
]
