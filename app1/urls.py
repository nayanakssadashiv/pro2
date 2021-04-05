from django.urls import path
from app1 import views
app_name="app1"
urlpatterns = [
    path("index/",views.index1,name="index1"),
    path("rend_app1/",views.rend_app1,name="rend_app1"),
]
