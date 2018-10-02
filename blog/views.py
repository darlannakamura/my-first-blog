from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST, request.FILES)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', slug=post.slug)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, slug):
     post = get_object_or_404(Post, slug=slug)
     if request.method == "POST":
         form = PostForm(request.POST, request.FILES, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', slug=post.slug)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})

def login(request):
    if request.method == "GET":
        return render(request, 'blog/login.html', {})

    if request.method == "POST":
        login = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=login, password=password)
        login(request, user)
        return redirect('post_list')


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        return render(request, 'blog/post_list.html', {'posts':posts})

class PostDetailView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        
        return render(request, 'blog/post_detail.html', {'post': self.get_object()})

class PostCreateView(CreateView):
    model = Post

    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', slug=post.slug)

class PostUpdateView(UpdateView):
    model = Post

    def get(self, request, *args, **kwargs):
        form = PostForm(instance=self.get_object())
        return render(request, 'blog/post_edit.html', {'form': form})

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)