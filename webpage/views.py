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
                param = {'mesgs': [{"sender": "ITS Help Desk is the subject and not the sender!"}, {"date": "Notice how the message says before 48 hours!"}]}
            elif 'sender' in form_detail.keys():
                param = {'mesgs': [{'sender': 'ITS Help Desk is the subject and not the sender!'}]}
            elif 'date' in form_detail.keys():
                param = {'mesgs': [{'date': 'Notice how the message says before 48 hours!'}]}
                
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
                param = {'mesgs': [{"date": "Notice that the subject of the email says important!"}, {"link": "Why are you being addressed as network user in the message?"}]}
            elif 'date' in form_detail.keys():
                param = {'mesgs': [{'date': 'Notice that the subject of the email says important!'}]}
            elif 'link' in form_detail.keys():
                param = {'mesgs': [{'link': 'Why are you being addressed as network user in the message?'}]}
                
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
                param = {'mesgs': [{"sender": "Notice that you are being asked for your PIN Number!"}, {"main": "They mention Bank of America but are they actually representing the organisation?"}]}
            elif 'sender' in form_detail.keys():
                param = {'mesgs': [{'sender': 'Notice that you are being asked for your PIN Number!'}]}
            elif 'main' in form_detail.keys():
                param = {'mesgs': [{'main': 'They mention Bank of America but are they actually representing the organisation?'}]}
                
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
                param = {'mesgs': [{"sender": "Unknown Number?"}, {"link": "Notice that there is no option to say NO!"}]}
            elif 'sender' in form_detail.keys():
                param = {'mesgs': [{'sender': 'Unknown Number?'}]}
            elif 'link' in form_detail.keys():
                param = {'mesgs': [{'link': 'Notice that there is no option to say NO!'}]}
                
            return render(request, 'phish1c.html', param)
        
        elif 'wrong' and 'right' not in [val for val in form_detail.values()]:
            return render(request, 'phish1c.html', {})
        
        elif all(val != 'wrong' for val in form_detail.values()):
            return render(request, 'index.html', {})
    else:
        return render(request, 'phish1c.html', {})

def phish2(request):
    if request.method == "POST":
        form_detail = request.POST
        print(form_detail)
        score = 0
        if 'right' in [val for val in form_detail.values()]:
            score += 1
            param = {'mesgs': [{"right": "You got right"}]}
        elif 'wrong' in [val for val in form_detail.values()]:
            score += 0
            param = {'mesgs': [{"wrong": "You got wrong"}]}
        elif 'right' and 'wrong' not in [val for val in form_detail.values()]:
            score += 0
            param = {'mesgs': [{"Don't leave any blank"}]}
        return render(request, 'phish2.html', param)
    # print("You got " + str(score) + "/" + str(len(form_detail)) + "correct out of 9")
    else:
        return render(request, 'phish2.html', {})

def phish3(request):
    return render(request, 'phish3.html', {})
# Create your views here.
