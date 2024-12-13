from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    cart_count = len(cart)  # Get the total number of items in the cart
    return render(request, 'cart_summary.html', {
        "cart_products": cart_products,
        "quantities": quantities,
        "totals": totals,
        "cart_count": cart_count  # Send cart_count to template
    })


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = len(cart)  # Get updated cart quantity
        cart_total = cart.cart_total()  # Get the updated cart total

        # Send updated cart quantity and total to frontend
        response = JsonResponse({'qty': cart_quantity, 'total': cart_total})
        messages.success(request, 'Product has been added to cart')
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        cart_quantity = len(cart)  # Get updated cart quantity
        cart_total = cart.cart_total()  # Get updated cart total

        # Send updated cart quantity and total to frontend
        response = JsonResponse({'qty': cart_quantity, 'total': cart_total})
        messages.success(request, 'Item has been deleted from cart')
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product_id=product_id, quantity=product_qty)



        cart_quantity = len(cart)  # Get updated cart quantity
        cart_total = cart.cart_total()  # Get updated cart total

        # Send updated cart quantity and total to frontend
        response = JsonResponse({'qty': cart_quantity, 'total': cart_total})
        messages.success(request, 'Your cart has been updated!')
        return response
