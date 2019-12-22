from django.contrib import admin
from django.urls import path
from xmlbeautifyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('output/',views.output,name="output"),
]
