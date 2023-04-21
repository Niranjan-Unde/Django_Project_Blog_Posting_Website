from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm,UserForm
from  django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from datetime import date
from django.db.models import Q

# Create your views here. 
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    allPost=Post.objects.order_by('-created_on').filter(status=1)  #filter active post by descending order
    return render(request,'index.html',{'allPost':allPost})


def create_post(request):
    user_id=request.user.id
    super_user=request.user.is_superuser
    if request.method == "POST":
        pform=PostForm(request.POST)
        try:
            if pform.is_valid():
                title=pform.cleaned_data["title"]
                sdetail=pform.cleaned_data["sdetail"]
                detail=pform.cleaned_data["detail"]
                cat=pform.cleaned_data["cat"]
                status=pform.cleaned_data["status"]

                p=Post(title=title,sdetail=sdetail,detail=detail,cat=cat,status=status,created_on=date.today(),uid=user_id)
                p.save()

                excludelst=['Cat','Status']
                pform=PostForm()
                return render(request,'createPost.html',{'msg':'Post Created Successfully!','pform':pform,'excludelst':excludelst})
        
        except Exception as e:
            print('Error:',e)
            excludelst=['Cat','Status']
            pform=PostForm()
            return render(request,'createPost.html',{'msg':'Failed to Creat Post!','pform':pform,'excludelst':excludelst})

    else:
        pform=PostForm()
        excludelst=['Cat','Status']
        return render(request,'createPost.html',{'pform':pform,'excludelst':excludelst})


def edit(request,rid):
    if request.method == 'POST':
        postToEdit=Post.objects.get(id=rid)
        pform=PostForm(request.POST,instance=postToEdit)
        if pform.is_valid():
            pform.save()
            return redirect('/udash')
        
    else:
        
        postToEdit=Post.objects.get(id=rid)   #Post.objects.filter(id=rid)
        
        pform=PostForm(instance=postToEdit)
        return render(request,'editform.html',{'pform':pform})

def delete(request,rid):
    p=Post.objects.get(id=rid)
    p.delete()
    return redirect("/udash")


def dashboard(request):
    user_id=request.user.id
    super_user=request.user.is_superuser

    if not super_user:
        p=Post.objects.filter(uid=user_id)
    else:
        p=Post.objects.all()
    return render(request,'dashboard.html',{'data':p})


def catfilter(request,catid):
    user_id=request.user.id
    super_user=request.user.is_superuser

    if not super_user:
        q1=Q(uid=user_id)
        q2=Q(cat=catid)
        p=Post.objects.filter(q1 & q2)
    else:
        p=Post.objects.filter(cat=catid)
    return render(request,'dashboard.html',{'data':p})


def actfilter(request,actid):
    user_id=request.user.id
    super_user=request.user.is_superuser

    if not super_user:
        q1=Q(uid=user_id)
        q2=Q(status=actid)
        p=Post.objects.filter(q1 & q2)
    else:
        p=Post.objects.filter(status=actid)
    return render(request,'dashboard.html',{'data':p})

def user_register(request):
    if request.method=='POST':
        uform=UserForm(request.POST)
        if uform.is_valid():
            uform.save()

            uform=UserForm()
            return render(request,'user_register.html',{'msg':'User Register Successfully!','uform':uform})

        else:
            uform=UserForm()
            return render(request,'user_register.html',{'msg':'Failed to Register!','uform':uform})
    else:
        uform=UserForm()
        return render(request,'user_register.html',{'uform':uform})

def user_login(request):
    if request.method == 'POST':
        lform=AuthenticationForm(request=request,data=request.POST)
        if lform.is_valid():
            uname=lform.cleaned_data['username']
            upass=lform.cleaned_data['password']

            u=authenticate(username=uname,password=upass)
            if u:
                login(request,u)
                return redirect('/')
                
        else:
            lform=AuthenticationForm()
            return render(request,'login.html',{'lform':lform,'msg':'Invalid username and/or password'})
    else:
        lform=AuthenticationForm()
        return render(request,'login.html',{'lform':lform})


def user_logout(request):
    logout(request)    #this function distroy session
    return redirect('/login')


def readMore(request,rid):
    postToView=Post.objects.get(id=rid)   #Post.objects.filter(id=rid)
    return render(request,'readMore.html',{'post':postToView})


