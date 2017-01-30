from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

def post_list(request):
    posts=Post.objects.all()
    return render(request,'sale_app/index.html',{'posts':posts})
    


def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'sale_app/detail.html',{'post':post})


def post_new(request):
    if request.method == "POST":
        form=PostForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.pub_date=timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm()
    return render(request,'sale_app/add_new.html',{'form':form})


    
def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form=PostForm(request.POST or None,request.FILES or None,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.pub_date=timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'sale_app/add_new.html',{'form':form})

def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sale_app/login/')
    else:
        form=UserCreationForm()
        return render(request,'sale_app/reg_form.html',{'form':form})

