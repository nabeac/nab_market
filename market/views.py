from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Category, Imgs


def home(request):
    threshold = 0
    discounted_products = Product.objects.filter(discount__gt=threshold)[:10]
    new_products = Product.objects.all().order_by('-id')[:10]

    return render(request, 'market/index.html', {
        'product': discounted_products,
        'new_products': new_products,

    })


def category(request, cat):
    categorys = cat.replace("-", " ")
    try:
        filter_cat = Category.objects.get(name=categorys)
        filter_product = Product.objects.filter(category=filter_cat)
        return render(request, 'market/category.html', {
            'product': filter_product,
            'category': filter_cat,
        })

    except:
        messages.success(request, ('404 این دسته بندی وجود ندارد '))
        return redirect('home')




def vue_product(request, pk):
    product = Product.objects.get(pk=pk)
    product_all = Product.objects.all()
    cat = [category.name for category in product.category.all()]
    result = ', '.join(cat)
    return render(request, 'market/single.html', {
        'product': product,
        'product_all': product_all,
        'cat': result,
    })
