from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    products_all = Product.objects.all()
    context = {
        'product_list': products_all,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name} \nТелефон: {phone} \nСообщение: {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    product_one = get_object_or_404(Product, pk=pk)
    context = {
        'product': product_one
    }
    return render(request, 'catalog/product.html', context)
