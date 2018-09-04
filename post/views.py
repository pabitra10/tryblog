from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def post_create(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form=PostForm()
    return render(request,'post/postnew.html',{'form':form})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'post/postdetails.html',{'post':post})

def post_list(request):
    post=Post.objects.all()
    return render(request,'post/postlist.html',{'post':post})
    

def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")