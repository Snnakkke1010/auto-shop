from django.db.models import Q
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ProductForm, ProductSearchForm
from .models import Product, ProductCategory


def home_page(request):
    return render(request, 'main/home.html')


def product_list(request):
    products = Product.objects.all()

    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(cat=category)

    in_stock = request.GET.get('in_stock')
    if in_stock:
        products = products.filter(in_stock=True)

    search_form = ProductSearchForm(request.GET)
    search_query = request.GET.get('search_query', '')
    if search_query:
        products = products.filter(Q(name__icontains=search_query))

    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories = ProductCategory.objects.all()

    return render(request, 'tasks/product_list.html', {'products': products, 'categories': categories, 'search': search_form})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'tasks/product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'tasks/add_product.html', {'form': form})