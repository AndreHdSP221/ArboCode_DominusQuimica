from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerar_csv_view, name='gerar_csv'),
]
