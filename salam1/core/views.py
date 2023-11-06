from django.shortcuts import render,redirect
from core.models import Profile,Post,Comment
from core.forms import PostForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from core.filters import PostFilter
def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.info(request,"Account is not active")
                return redirect('login')
        else:
            messages.info(request,"الرجاء إدخال اسم المستخدم وكلمة السر الصحيحين")
            return redirect('login')
    else:
        return render(request,'auth/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def index(request):
    posts = Post.objects.all()
    content = {
        'posts':posts,
        'filter':PostFilter(),
        'form':CommentForm(),
    }
    return render(request,'index.html',context=content)


def post_filter(request):

    title = request.GET.get('title')
    desc = request.GET.get('desc')
    posts = Post.objects.filter(title=title,desc=desc)
    content = {
        'posts':posts,
        'filter':PostFilter(),
        'form':CommentForm(),
    }
    return render(request, 'index.html',content)

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
        else:
            form = PostForm()
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request,'create.html', context=context)

@login_required
def update(request, id):
    post = Post.objects.get(id=id)
    if post.author != request.user:
        return HttpResponseForbidden()
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
            # return redirect('post_detail', pk=post.id)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'update.html', context=context)

@login_required
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('posts')


@login_required
def post_comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('posts')
        else:
            form = CommentForm()
    else:
        form = CommentForm()
            
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'comments/create.html', context=context)
    

def comment_delete(request,id):
    Comment.objects.get(id=id).delete()
    return redirect('posts')


def comment_update(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:    
            form = CommentForm()
    else:
        form = CommentForm(instance=comment)
            
    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, 'comments/create.html', context=context)

    