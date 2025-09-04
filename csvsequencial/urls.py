from django.urls import path
from . import views

app_name = 'qrcode'
urlpatterns = [
    path('', views.gerar_csv, name='gerar_csv'),
]
