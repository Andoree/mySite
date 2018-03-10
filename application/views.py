from django.shortcuts import render


def post_page(request):
    return render(request, 'application/post_list.html', {})


def post_page1(request):
    return render(request, 'application/page1.html', {})

def post_page2(request):
    return render(request, 'application/page2.html', {})

def post_page3(request):
    return render(request, 'application/page3.html', {})

# Create your views here.
