from django.shortcuts import render
from django.contrib.auth.models import User,auth

def track(request):
    name=User.username
    return render(request,"index.html")
