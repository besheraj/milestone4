from django.shortcuts import render


def index(request):
    # view the index page

    return render(request, 'home/index.html')
