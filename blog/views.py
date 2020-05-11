from django.shortcuts import render,redirect
from .models import post
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required


class PostForm(ModelForm):
    class Meta:
            model=post
            fields=['title','body','author']


@login_required(login_url='accounts')
def blog_request_view(request):
    if request.method=="GET":
        posts=post.objects.all()
        
        context={
            'posts':posts
        }
        return render(request,'blog/index.html',context=context)
    

@login_required(login_url='accounts')
def delete_post_handler(request,id):
    print(id)
    if request.method=="GET":
        p=post.objects.get(id=id)
        p.delete()
        return redirect('blog') 
        

@login_required(login_url='accounts')
def blog_request_details(request,id):

    if request.method=="GET":
        p=post.objects.get(id=id)
        context={
            'post':p
        }
        return render(request,'blog/about.html',context=context)



@login_required(login_url='accounts')
def create_blog_request(request): 
    if request.method=="GET":
        form=PostForm()
        for _ in form.fields:
            form.fields[_].widget.attrs={'maxlength': '200',"class":"form-control"}
        context={"form":form}
        return render(request,'blog/create.html',context=context)
    elif request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved and valid')
            return redirect('blog')
        else: 
           return redirect('create')
