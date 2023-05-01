from django.shortcuts import render, redirect
from .models import Sms1
#from .forms import Sms1Form

def index(request):
    all_members = Sms1.objects.all
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def recc(request):
    return render(request, 'recc.html', {})

def phish1(request):
    if request.method == "POST":
        form_detail = request.POST
        print(form_detail)
        if 'wrong' in [val for val in form_detail.values()]:
            if 'sender' and 'date' in form_detail.keys():
                param = {'mesgs': [{"sender": "Clearly check if you can identify the sender!"}, {"date": "Clearly check that the date matters!"}]}
            elif 'sender' in form_detail.keys():
                param = {'mesgs': [{'sender': 'Clearly check if you can identify the sender!'}]}
            elif 'date' in form_detail.keys():
                param = {'mesgs': [{'date': 'Clearly check that the date matters!'}]}
                
            return render(request, 'phish1.html', param)
        
        elif 'wrong' and 'right' not in [val for val in form_detail.values()]:
            return render(request, 'phish1.html', {})
        
        elif all(val != 'wrong' for val in form_detail.values()):
            return render(request, 'phish1a.html', {})
    else:
        return render(request, 'phish1.html', {})

def phish1a(request):
    if request.method == "POST":
        form_detail = request.POST
        print(form_detail)
        if 'wrong' in [val for val in form_detail.values()]:
            if 'date' and 'link' in form_detail.keys():
                param = {'mesgs': [{"date": "Clearly check if you can identify the sender!"}, {"link": "Clearly check that the date matters!"}]}
            elif 'date' in form_detail.keys():
                param = {'mesgs': [{'date': 'Notice that the subject of the email says "important"!'}]}
            elif 'link' in form_detail.keys():
                param = {'mesgs': [{'link': 'Clearly check that the date matters!'}]}
                
            return render(request, 'phish1a.html', param)
        
        elif 'wrong' and 'right' not in [val for val in form_detail.values()]:
            return render(request, 'phish1a.html', {})
        
        elif all(val != 'wrong' for val in form_detail.values()):
            return render(request, 'phish1b.html', {})
    else:    
        return render(request, 'phish1a.html', {})

def phish1b(request):
    if request.method == "POST":
        form_detail = request.POST
        print(form_detail)
        if 'wrong' in [val for val in form_detail.values()]:
            if 'sender' and 'main' in form_detail.keys():
                param = {'mesgs': [{"sender": "Clearly check if you can identify the sender!"}, {"main": "Clearly check that the date matters!"}]}
            elif 'sender' in form_detail.keys():
                param = {'mesgs': [{'sender': 'Notice that the subject of the email says "important"!'}]}
            elif 'main' in form_detail.keys():
                param = {'mesgs': [{'main': 'Clearly check that the date matters!'}]}
                
            return render(request, 'phish1b.html', param)
        
        elif 'wrong' and 'right' not in [val for val in form_detail.values()]:
            return render(request, 'phish1b.html', {})
        
        elif all(val != 'wrong' for val in form_detail.values()):
            return render(request, 'phish1c.html', {})
    else:    
        return render(request, 'phish1b.html', {})

def phish1c(request):
    if request.method == "POST":
        form_detail = request.POST
        print(form_detail)
        if 'wrong' in [val for val in form_detail.values()]:
            if 'sender' and 'link' in form_detail.keys():
                param = {'mesgs': [{"sender": "Clearly check if you can identify the sender!"}, {"link": "Clearly check that the date matters!"}]}
            elif 'sender' in form_detail.keys():
                param = {'mesgs': [{'sender': 'Notice that the subject of the email says "important"!'}]}
            elif 'link' in form_detail.keys():
                param = {'mesgs': [{'link': 'Clearly check that the date matters!'}]}
                
            return render(request, 'phish1c.html', param)
        
        elif 'wrong' and 'right' not in [val for val in form_detail.values()]:
            return render(request, 'phish1c.html', {})
        
        elif all(val != 'wrong' for val in form_detail.values()):
            return render(request, 'index.html', {})
    else:
        return render(request, 'phish1c.html', {})

def phish2(request):
    return render(request, 'phish2.html', {})

def phish3(request):
    return render(request, 'phish3.html', {})
# Create your views here.
