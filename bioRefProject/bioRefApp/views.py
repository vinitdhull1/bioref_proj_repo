from os.path import basename
from django.conf import settings
import os, glob
from os import path
from zipfile import ZipFile
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import shutil
import datetime
import io
from io import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai_model_output import biorefOutput

# Create your views here.
@login_required(login_url='login')
def index(request):
    data = ""
    if request.method == "POST":
        data = request.POST.get("para")
        print(data)
        bioref_output = biorefOutput(data)
        context = {
            "item": bioref_output,
            "data": data
        }
        return render(request, "index.html", context)
    else:
        context = {
            "item": "none",
        }
        return render(request, "index.html", context)



def log_in(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        context = {}
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # return render(request, 'index.html')
                return redirect(index)
            else:
                messages.error(request, 'please enter correct credentials!')
                return render(request, 'login.html', context)
        else:
            return render(request, 'login.html')

@login_required(login_url='login')
def log_out(request):
    auth.logout(request)
    return render(request, 'login.html')