from django.shortcuts import render, redirect, get_object_or_404
from .models import Store, Category, Product
from slugify import slugify


def main(request):
    stores = Store.objects.all()
    ctx = {
        'stores': stores
    }
    return render(request=request, template_name='store_app/main.html', context=ctx)


def add_store(request):
    if request.method == "POST":
        store_name = request.POST.get('store_name',)
        store_address = request.POST.get('store_address',)

        store_slug = slugify(store_name)
        new_store = Store(name=store_name, address=store_address, slug=store_slug)
        new_store.save()
        return redirect('main')
    return render(request, 'store_app/main.html')


def delete_store(request, slug):
    store = get_object_or_404(Store, slug=slug)
    store.delete()
    return redirect('main')


def edit_store(request, slug):
    store = get_object_or_404(Store, slug=slug)
    if request.method == "POST":
        store_name = request.POST.get('store_name')
        store_address = request.POST.get('store_address')
        store_slug = slugify(store_name)
        store.name = store_name
        store.address = store_address
        store.slug = store_slug
        store.save()
        return redirect('main')
    return render(request, 'store_app/edit_store.html', {'store': store})


def category(request):
    categories = Category.objects.all()
    ctx = {
        'categories': categories
    }
    return render(request=request, template_name='store_app/category.html', context=ctx)


def add_category(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name',)

        category_slug = slugify(category_name)
        new_category = Category(name=category_name, slug=category_slug)
        new_category.save()
        return redirect('category')
    return render(request, 'store_app/category.html')


def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category.delete()
    return redirect('category')


def edit_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        category_slug = slugify(category_name)
        category.name = category_name
        category.slug = category_slug
        category.save()
        return redirect('category')
    return render(request, 'store_app/edit_category.html', {'category': category})


def products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    ctx = {
        'category': category,
        'products': products
    }
    return render(request=request, template_name='store_app/products.html', context=ctx)


def add_product(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_quantity = request.POST.get('product_quantity')
        category_id = request.POST.get('product_category')
        store_ids = request.POST.getlist('product_stores')

        category = Category.objects.get(id=category_id)
        product_slug = slugify(product_name)

        new_product = Product(
            name=product_name,
            price=product_price,
            quantity=product_quantity,
            category=category,
            slug=product_slug
        )
        new_product.save()

        stores = Store.objects.filter(id__in=store_ids)
        new_product.store.set(stores)
        new_product.save()

        return redirect('category')
    else:
        categories = Category.objects.all()
        stores = Store.objects.all()
        return render(request, 'store_app/add_product.html', {'categories': categories, 'stores': stores})


def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.delete()
    return redirect('category')


def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_quantity = request.POST.get('product_quantity')
        product_slug = slugify(product_name)
        product.name = product_name
        product.price = product_price
        product.quantity = product_quantity
        product.slug = product_slug
        product.save()
        return redirect('category')
    return render(request, 'store_app/edit_product.html', {'product': product})
