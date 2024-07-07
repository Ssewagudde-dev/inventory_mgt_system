from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
# Home View
def home_view(request):
    return render(request, 'invApp/home.html')


# Add Product View
def add_product_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    # context = {'form': form}
    return render(request, 'invApp/product_form.html', {'form': form})


# Products list view

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})

# Update Product
def update_product_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})


# Delete Product

def delete_product_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()    
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})
