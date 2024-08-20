from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'core/index.html')


def blog(request):
    return render(request, 'core/blog.html')


def about(request):
    return render(request, 'core/about.html')
