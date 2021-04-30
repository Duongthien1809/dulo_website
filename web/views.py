from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import LoginForm, RegisterForm, PostModelForm
from .models import PostModel
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView


def base(request):
    post_view = PostModel.objects.all()
    return render(request, 'web/base.html', {'post_view': post_view})


def login_view(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('web:base')
    return render(request, 'web/login.html', {'login_form': login_form})


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('web:registration_ok')
    return render(request, 'web/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('web:base'))


def upload_view(request):
    post_form = PostModelForm()
    if request.method == 'POST':
        post_form = PostModelForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
        return redirect('web:base')
    return render(request, 'web/posten.html', {'post_form': post_form})


def registrationok_view(request):
    return render(request, 'web/registration_ok.html')


class PostListView(ListView):
    template_name = 'web/posten_list.html'
    queryset = PostModel.objects.all()


def profile_view(request):
    # profile_detail = User.objects.get(id=2)
    return render(request, 'web/Profile.html')


def search(request):
    try:
        query = request.POST['query']
    except MultiValueDictKeyError:
        query = False
    allposts = PostModel.objects.filter(title=query)
    params = {'allposts': allposts, 'query': query}
    return render(request, 'web/search.html', params)


def delete_view(request, pk):
    if request.method == "POST":
        obj = PostModel.objects.get(id=pk)
        obj.delete()
    return redirect('web:list_view')



def PostDetailView(request, pk):
    obj = get_object_or_404(PostModel, id=pk)
    context = {
        'obj': obj
    }
    return render(request, 'web/Post_detail.html', context)


def update_view(request, pk):
    obj = PostModel.objects.get(id=pk)
    post_form = PostModelForm(instance=obj)
    if request.method == 'POST':
        post_form = PostModelForm(request.POST, request.FILES, instance=obj)
        if post_form.is_valid():
            update_post = post_form.save(commit=False)
            update_post.save()
            return redirect(reverse('web:base'))
    context = {'form': post_form}
    return render(request, 'web/update_view.html', context)

def einkaufenView(request):
    return render(request, 'web/Einkaufen.html')
