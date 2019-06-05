from django.shortcuts import render,redirect
from .forms import Businessform,ProfileForm
from .models import Users,Business

# Create your views here.


def index(request):
    business=Business.objects.all()
    return render(request,'index.html',{'business':business})

def dashboard(request):
    user_id=Users.objects.filter(user=request.user)
    id=0
    for i in user_id:
        id+=i.id




    if request.method=='POST':
        form=Businessform(request.POST,request.FILES)
        if form.is_valid():
            business=form.save(commit=False)
            business.user=request.user
            business.users=Users(id)
            business.save()
        return redirect('home')
    else:
        form=Businessform()

    return render(request,'dashboard.html',{'form':form})

def profile(request):
    try:
        profiles=Users.objects.filter(user=request.user)
    except Exception as e:
        raise Http404()
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
        return redirect('profile')
    else:
        form=ProfileForm()

    return render(request,'profile.html',{'form':form,'profiles':profiles})
