from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Needrequest
from Userprofile.models import Profile
import donator;
import Userprofile;


@login_required
def needrequest(request):
    if request.method == 'POST':
        if  request.POST.get("title",False) and request.POST.get("body", False) and request.POST.get('name', False) and  request.POST.get('phone', False):
            _request =  Needrequest()
            _request.title = request.POST.get('title',False)
            _request.body = request.POST.get('body', False)
            _request.name = request.POST.get('name', False)
            _request.phone = request.POST.get('phone', False)
            _request.pub_date = timezone.datetime.now()
            _request.needy = request.user
            for i in Profile.objects.all():
                if(i.profile_owner==_request.needy):
                    _request.save()
                    return render(request, 'req_details.html',{"request": _request})
                
            return render(request, 'Pform.html',{'error':'create your profile first'})
                
        return render(request, 'need_request.html',{'error':'All fields are required'})
    
    return render(request, 'need_request.html')


def delete1(request):
        if request.method=="POST":
            for req in Needrequest.objects.all():
                if(request.user== req.needy):
                    req.delete() 
                    return render(request, 'delete1.html')
                
    
def info1(request, request_id):
    request1 = get_object_or_404(Needrequest,pk= request_id)
    return render(request,'info1.html',{'request':request1})

def delete(request, request_id):
        request1 = get_object_or_404(Needrequest,pk= request_id)
        request1.delete()
        return redirect('displayrequest')



def edit(request, id):
    _request = get_object_or_404(Needrequest, pk=id)
    if request.method=="POST":
        if request.POST.get("title",False) and request.POST.get("body", False) and request.POST.get('name', False) and request.POST.get('phone', False):
            _request.title = request.POST.get('title',False)
            _request.body = request.POST.get('body', False)
            _request.phone = request.POST.get('phone', False)
            _request.name = request.POST.get('name', False)
            _request.pub_date = timezone.datetime.now()
            _request.needy = request.user
            _request.save()
            return redirect('displayrequest')
            
        return render(request, "index7.html", {"error":"fill all the inputs", "id": id })		
    return render(request, "index7.html",{"id":id})

def displayrequest(request):
    request1 = Needrequest.objects.all()
    return render(request,'displayrequest.html',{'requests':request1})