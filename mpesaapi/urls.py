from django.urls import path
from . import views

urlpatterns = [
    path('stk_push/', views.stk_push, name='stk_push'),
    path('callback/', views.callback, name='callback'),
    path('mpesa/', views.mpesa, name='mpesa'),
]
