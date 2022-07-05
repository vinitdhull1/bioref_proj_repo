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
from .models import InputInfo
from io import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai_model_output import biorefOutput

# Create your views here.
@login_required(login_url='login')
def index(request):
    data = ""
    if request.method == "POST" and request.POST.get("form_type") == "formOne":
        data = request.POST.get("para")
        print(data)
        bioref_output = biorefOutput(data)
        context = {
            "item": bioref_output,
            "data": data
        }
        return render(request, "index.html", context)
    elif request.method == "POST" and request.POST.get("form_type") == "formTwo":
        inpt = request.POST.get("input_text")
        otpt = request.POST.get("output_text")
        time_stamp = str(datetime.datetime.now().strftime("%Y-%m-%d--|--%H:%M"))
        data_obj = InputInfo(user_name=request.user, time_of_process=time_stamp, input_data=inpt, output_data=otpt)
        try:
            data_obj.save()
            context = {
                "item": otpt,
                "data": data
            }
            messages.success(request, "Your data saved successfully!")
        except:
            messages.error(request, "Oops! something went wrong.")
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