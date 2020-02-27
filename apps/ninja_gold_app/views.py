from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    context = {
        'gold' : request.session['gold']
    }
    return render(request, 'index.html', context)

def process_money (request):
    if request.POST ['building'] == 'farm':
        request.session['gold'] += random.randint(10, 20)

    elif request.POST ['building'] == 'cave':
        request.session['gold'] += random.randint(5, 10)

    elif request.POST ['building'] == 'house':
        request.session['gold'] += random.randint(2, 5)
        
    else:
        request.session['gold'] += random.randint(-50, 50)
    return redirect('/')

def destroy_session(request):
    request.session.clear()
    return redirect('/')
