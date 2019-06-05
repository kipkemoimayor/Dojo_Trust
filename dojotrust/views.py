from django.shortcuts import render,redirect
from .forms import Businessform,ProfileForm
from .models import Users,Business
from django.contrib.auth.decorators import login_required
from star_ratings.models import Rating
# Create your views here.


def index(request):
    business=Business.objects.all()[::-1]
    estate=Business.objects.filter(category='real').all()
    cars=Business.objects.filter(category='cars').all()
    agriculture=Business.objects.filter(category='agri').all()
    wear=Business.objects.filter(category='wear').all()
    rate=Rating.objects.all()
    top=0;
    idi=0
    for t in rate:
        if t.average>top:
            top=t.average
            idi=t.object_id

    topRate=Business.objects.filter(id=idi)[:1]
    title='Dojo Home'
    return render(request,'index.html',{'business':business,'title':title,'estate':estate,'cars':cars,'agriculture':agriculture,'wear':wear,'top':topRate,'count':round(top,1)})

@login_required(login_url='/accounts/login/')
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

def single_business(request,business_id):
    try:
        rate=Rating.objects.filter(object_id=business_id)
        ave=0
        for j in rate:
            ave+=j.average

        if ave>=5:
            message='This Product Is recommended'
        else:
            message='Make a decision'
    except Exception as e:
        raise Http404()
    busi=Business.objects.filter(pk=business_id).first()
    business=Business.objects.filter(pk=business_id)
    return render(request,'single_business.html',{"business":business,'busi':busi,'message':message})
