from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
from .models import BlogModel

from .form import *
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def airlift(request):
    return render(request, 'airlift.html')

def wildearth(request):
    return render(request, 'wildearth.html')

def home(request):
    blogs_list = BlogModel.objects.all()

    p = Paginator(blogs_list, 3)

    print(p.num_pages)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page = p.page(page_num)

    context = {'blogs': page}
    return render(request, 'home.html', context)


def login_view(request):
    return render(request, 'login.html')


def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)


def see_blog(request):
    context = {}

    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_blog.html', context)


def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(blog_obj)
            return redirect('/add-blog/')
    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)


def blog_update(request, slug):
    context = {}
    try:

        blog_obj = BlogModel.objects.get(slug=slug)

        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            blog_obj = BlogModel.objects.get(slug=slug)       
            blog_obj.delete()


            if form.is_valid():
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_blog.html', context)


def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-blog/')


def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')


def career(request):
    jobs_list = Job.objects.all()
    p = Paginator(jobs_list, 3)

    print(p.num_pages)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    page = p.page(page_num)

    context = {'jobs': page}
    return render(request, 'career.html', context)

def job_detail(request, slug):
    context = {}
    try:
        job_obj = Job.objects.filter(slug=slug).first()
        context['job_obj'] = job_obj
    except Exception as e:
        print(e)
    return render(request, 'job_detail.html', context)


def see_job(request):
    context = {}

    try:
        job_objs = Job.objects.filter(user=request.user)
        context['job_objs'] = job_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_job.html', context)


def add_job(request):
    context = {'form': JobForm}
    try:
        if request.method == 'POST':
            form = JobForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                description = form.cleaned_data['description']

            job_obj = Job.objects.create(
                user=user, title=title,
                description=description, image=image
            )
            print(job_obj)
            return redirect('/add-job/')
    except Exception as e:
        print(e)

    return render(request, 'add_job.html', context)


def job_update(request, slug):
    context = {}
    try:

        job_obj = Job.objects.get(slug=slug)

        if job_obj.user != request.user:
            return redirect('/')

        initial_dict = {'description': job_obj.description}
        form = JobForm(initial=initial_dict)
        if request.method == 'POST':
            form = JobForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                description = form.cleaned_data['description']

            job_obj = Job.objects.create(
                user=user, title=title,
                description=description, image=image
            )

        context['job_obj'] = job_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_job.html', context)


def job_delete(request, id):
    try:
        job_obj = Job.objects.get(id=id)

        if job_obj.user == request.user:
            job_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-job/')