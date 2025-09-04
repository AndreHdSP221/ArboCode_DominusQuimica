from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def gerar_csv(request: HttpRequest) -> HttpResponse:
    return render(request)