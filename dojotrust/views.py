from django.shortcuts import render
from .forms import Businessform
from .models import Users,Business

# Create your views here.


def index(request):
    return render(request,'index.html')

def dashboard(request):
    if request.method=='POST':
        form=Businessform(request.POST,request.FILES)
        if form.is_valid():
            business=form.save(commit=False)
            business.user=request.user
            business.users=Users(request.user.id)
            business.save()
        return redirect('home')
    else:
        form=Businessform()

    return render(request,'dashboard.html',{'form':form})

def profile(request):

    return render(request,'profile.html')
