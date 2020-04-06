from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('calculator.html',views.go,name='go'),
    path('submitquery',views.submitquery,name='submitquery')
]