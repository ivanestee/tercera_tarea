from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ClienteForm
from .models import Categoria, Producto, Cliente

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_categoria')  
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})  
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto') 
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_cliente')  
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})
