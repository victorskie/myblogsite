from django.shortcuts import render, redirect
from .forms import BlogPostForm, BlogUpdateForm
from .models import BlogPost
from django.http import HttpResponseRedirect


def home(request):
    return render(request, "home.html")

def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = BlogPostForm()  
    
    return render(request, 'create_blog.html', {'form': form})

def blog_titles(request):
    blog_posts = BlogPost.objects.all()  # Retrieve all blog posts
    return render(request, 'blog_titles.html', {'blog_posts': blog_posts})

def blog_description(request, pk):
    blog_post = BlogPost.objects.get(id=pk)
    return render(request, 'blog_description.html', {'blog_post': blog_post})

def delete_blog(request, pk):
    blog_post = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        blog_post.delete()
        return HttpResponseRedirect('/blog-titles/')
    return render(request, 'confirm_delete.html', {'blog_post': blog_post})

def blog_update_view(request, id):
    blogid = BlogPost.objects.get(id=id)
    if request.method == "POST":
        form = BlogUpdateForm(request.POST, instance = blogid)
        if form.is_valid():
            form.save()
            return redirect('blog_titles')
    else:
        form = BlogUpdateForm(instance = blogid)
    return render(request, 'blog_update.html', {'form': form})



student = {'name':'john', 'age':20 , 'cintent':'ttdgdhgfghfhf'}

