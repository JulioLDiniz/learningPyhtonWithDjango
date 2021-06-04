from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
# Create your views here.

def home(request):
    data = {}
    data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    data['form'].fields['modelo'].disabled = True
    data['form'].fields['marca'].disabled = True
    data['form'].fields['ano'].disabled = True
    data['visualizacao'] = True
    return render(request, 'form.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)

    #Aqui o parâmetro instance já reconhece o Carros como instância para construçção do CarrosForm
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update (request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete (request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')