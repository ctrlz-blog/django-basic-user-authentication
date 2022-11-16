from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:

    if request.user.is_authenticated:
        message = f"Hello {request.user.username}. You are logged in."
    else:
        message = "You are not logged in."
        
    context = {
        "message": message
    }

    return render(request, "core/index.html", context)