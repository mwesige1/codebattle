
from django.shortcuts import render,redirect
from . models import Event,User,Submission
from .forms import SubmissionForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    users = User.objects.filter(participart=True)
    event = Event.objects.all()

    context ={
        'users':users,
        'events':event,
    }
    return render(request,('home.html'),context)


def event_page(request, pk):
    event = Event.objects.get(pk=pk)
    #check if the the user already regustered
    registered = request.user.events.filter(id=event.id).exists()
    #check if the user already submitted
    submitted = Submission.objects.filter(participant=request.user,event= event).exists()
    

    context = {
        'event': event,
        'registered':registered,
        'submitted':submitted,
    }
    return render(request, 'event.html', context)


def event_register(request,pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        # go the event model and add the current logged in user
        event.participants.add(request.user)
        
        # redirect the to the axact page eveent
        return redirect('event',pk= event.id)

    return render(request,'event-confirm.html',{'even':event} )


def user_profile(request,pk):
    user = User.objects.get(id=pk)
    return render(request,'profile.html',{'user':user})


@login_required
def account_page(request):
    user = request.user
    return render(request,'account.html' ,{'user':user})

def project_submission(request,pk):
    event = Event.objects.get(id=pk)
    form = SubmissionForm()
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submissionform = form.save(commit=False)
            submissionform.participant = request.user
            submissionform.event = event 
            submissionform.save()
            return redirect('account')

    return render(request, 'submission.html' ,{'event':event,'form':form})

@login_required
def update_submission(request,pk):
    submissin = Submission.objects.get(id=pk)

    if request.user != submissin.participant:
        return HttpResponse('You are not supposed to be here')
        
    form = SubmissionForm(instance=submissin)

    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=submissin)
        if form.is_valid():
            form.save()
            return redirect('account')
    event = Submission.event

    context ={
        'form':form,
        'event':event,
    }
    return render (request,'submission.html',context)


def login_page(request):
    page = 'login'
    if request.method == 'POST':
        user = authenticate(email=request.POST['email'],password= request.POST['password'])
        if not None:
            login(request,user)
            return redirect('home')

    context={
        'page':page,
    }
    return render(request,'login.html',context)


def logout_user(request):
    logout(request)
    return redirect('login')

def register_page(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('home')
        
    page = 'register'
    context={
        'page':page,
        'form':form,
    }
    return render(request,'login.html',context)