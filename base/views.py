from django.shortcuts import render,HttpResponseRedirect, redirect
from .forms import PetientRegistration
from .models import User

# Create your views here.
def add(request):
    if request.method == 'POST':
        fm = PetientRegistration(request.POST)
        if fm.is_valid():
            fnm = fm.cleaned_data['firstname']
            lnm = fm.cleaned_data['lastname']
            gd = fm.cleaned_data['gender']
            ds = fm.cleaned_data['Disease']
            dc = fm.cleaned_data['doctor']
            df = fm.cleaned_data['doctor_fees']
            ad = fm.cleaned_data['admit_date']
            reg = User(firstname=fnm,lastname=lnm,gender=gd,Disease=ds,doctor=dc,doctor_fees=df,admit_date=ad)
            reg.save()
            fm = PetientRegistration()
    else:
        fm = PetientRegistration()
    stud = User.objects.all()
    return render(request, 'index.html',{'form':fm})

def show(request):
    stud = User.objects.all()
    return render(request, 'list.html',{'stu':stud})

def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = PetientRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = PetientRegistration(instance=pi)
    return render(request, 'update.html',{'form':fm})

def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('list')