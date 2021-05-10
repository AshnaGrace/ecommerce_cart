from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from ecommerce.models import category, product


def allCat(request,c_slug=None):
    cpage=None
    products_list=None
    if c_slug!=None:
        cpage=get_object_or_404(category,slug=c_slug)
        products_list=product.objects.filter(category=cpage,available=True)
    else:
        products_list=product.objects.all().filter(available=True)
    paginator = Paginator(products_list,6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':cpage,'products':products})

def proddetail(request, c_slug, product_slug):
    try:
        product1=product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product1})


