from django.shortcuts import render

# Create your views here.

def programme(request):

    return render(request, 'programmes')


def build_muscle(request):
    print("HEEEERRREE")

    return render(request, 'programmes/build_muscle.html')


def get_lean(request):

    return render(request, 'programmes/get_lean.html')


def lose_weight(request):

    return render(request, 'programmes/lose_weight.html')

def membership(request):

    return render(request, 'programmes/membership.html')
