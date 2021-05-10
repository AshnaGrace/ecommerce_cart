from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from ecommerce.models import product

# Create your views here.
from cart.models import Cart, cartitem


def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create
    return cart
def add_cart(request,product_id):
    product2=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item=cartitem.objects.get(product=product2,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1
            cart_item.save()
    except cartitem.DoesNotExist:
        cart_item=cartitem.objects.create(
            product=product2,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return redirect('cart:cart_detail')
def cart_detail(request,total=0,count=0,cartitems=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cartitems=cartitem.objects.filter(cart=cart,active=True)
        for cart_item in cartitems:
            total+=(cart_item.product.price * cart_item.quantity)
            count+=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cartitems=cartitems,total=total,count=count))
def cart_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product1=get_object_or_404(product,id=product_id)
    cart_item=cartitem.objects.get(product=product1,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product1 = get_object_or_404(product, id=product_id)
    cart_item = cartitem.objects.get(product=product1, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')