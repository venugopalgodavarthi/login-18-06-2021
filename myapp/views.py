from django.shortcuts import render,reverse
from myapp import forms 
from myapp import models 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def base(request):
    return render(request,"base.html")

def Register(request):
    form = forms.Reg()
    if request.method=="POST":
        form=forms.Reg(request.POST)
        if form.is_valid():
            #form.save(commit=True)
            messages.success(request,"registration successfull.")
            #return HttpResponseRedirect(reverse('login'))
            
    return render(request,"register.html",{'form':form})


def Login(request):
    form = forms.Login()
    if request.method=="POST":
        form=forms.Login(request.POST)
        if form.is_valid():
            print(request.POST)
            p1=models.login.objects.filter(email= form.cleaned_data['usermail'],
                                        password=form.cleaned_data['password'],)
            return HttpResponseRedirect(reverse('home'))
    return render(request,"login.html",{'form':form})

def Home(request):
    return render(request,"home.html")
    


