from django import forms
from django.shortcuts import render,redirect
from .forms import optionForm
import re

def extractdates(test_string):
    match_str = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', test_string)
    res = list(map(str, match_str))
    return str(res)

def Number(test_string):
    temp = re.findall(r'([1-9]\d\d|[1-9]\d{3,})', test_string)
    res = list(map(int, temp))
    return str(res)

def isValidIP(str):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    p=re.compile(regex)
    if(re.search(p,str)):
        return True
    else:
        return False  


def isValidEmail(str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    p=re.compile(regex)
    if(re.search(p,str)):
        return True
    else:
        return False    

def isValidMACAddress(str):

    regex = ("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

    p = re.compile(regex)
    if(re.search(p, str)):
        return True
    else:
        return False

def change_case(str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def home(request):
    submitbutton = request.POST.get("submit")
    input=""
    choice=""
    output=""
    form=optionForm(request.POST)
    if form.is_valid():
        input=form.cleaned_data.get("Input")
        choice = form.cleaned_data.get("options")
        if(choice == "1"):
            output=Number(input)
        if(choice == "2"):
            output=extractdates(input)
        if(choice=="4"):
            answer = isValidEmail(input)
            if(answer):
                output = "Valid Email address"
            else:
                output = "not a valid email address"
        if(choice=="5"):
            answer = isValidIP(input)
            if(answer):
                output = "Valid IP address"
            else:
                output = "not a valid IP address"
        if(choice=="6"):
            answer = isValidMACAddress(input)
            if(answer):
                output = "Valid MAC address"
            else:
                output = "not a valid mac address"
        if(choice == "7"):
            output = change_case(input)
    context = {
        'form': form,
        'Output':output

    }
    return render(request, 'home/home.html' , context)


            
  




