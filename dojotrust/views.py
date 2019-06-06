from django.shortcuts import render,redirect
from .forms import Businessform,ProfileForm,ReviewForm
from .models import Users,Business,Reviews
from django.contrib.auth.decorators import login_required
from star_ratings.models import Rating
from django.http import HttpResponse,Http404
# Create your views here.


def index(request):
    business=Business.objects.all()[::-1]
    estate=Business.objects.filter(category='real').all()
    cars=Business.objects.filter(category='cars').all()
    agriculture=Business.objects.filter(category='agri').all()
    wear=Business.objects.filter(category='wear').all()
    rate=Rating.objects.all()
    reviews=Reviews.objects.all()
    top=0;
    idi=0
    for t in rate:
        if t.average>top:
            top=t.average
            idi=t.object_id

    topRate=Business.objects.filter(id=idi)[:1]
    title='Dojo Home'
    return render(request,'index.html',{'business':business,'title':title,'estate':estate,'cars':cars,'agriculture':agriculture,'wear':wear,'top':topRate,'count':round(top,1),'reviews':reviews})

@login_required(login_url='/accounts/login/')
def dashboard(request):
    user_id=Users.objects.filter(user=request.user)
    profile=Users.objects.filter(user=request.user)
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

    return render(request,'dashboard.html',{'form':form,'profile':profile})

def profile(request):
    try:
        profiles=Users.objects.filter(user=request.user)
        business=Business.objects.filter(user=request.user)
        reviews=Reviews.objects.filter(user=request.user)
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

    name=''
    for na in profiles:
        name=na.name

    new_name=name.split(" ")
    if len(new_name)>=2:

        newName=new_name[0][0]+new_name[1][0]
    else:
        newName=''
    if request.method=='POST':
        instance=Users.object.get(user=request.user)
        update_form=ProfileForm(request.POST,request.FILES,instance=instance)
        if update_form.is_valid():
            update=update_form.save(commit=False)
            profile.save()
        return redirect('profile')
    else:
        update_form=ProfileForm()


    return render(request,'profile.html',{'form':form,'update_form':update_form,'profiles':profiles,'name':newName,'business':business,'reviews':reviews})
@login_required(login_url='/accounts/login/')
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
    profile=Users.objects.filter(user=request.user)
    reviews=Reviews.objects.filter(business=business_id)
    if request.method=='POST':
        form=ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review=form.save(commit=False)
            review.user=request.user
            review.profile=Users(request.user.id)
            review.business=Business(business_id)
            review.save()

        return redirect("single",business_id)
    else:
        form=ReviewForm()
    return render(request,'single_business.html',{"business":business,'busi':busi,'message':message,'form':form,'profile':profile,'reviews':reviews})
