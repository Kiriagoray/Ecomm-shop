from shop.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the cart from the session or initialize it
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)

        # If the product is already in the cart, update the quantity
        if product_id in self.cart:
            self.cart[product_id] += int(quantity)
        else:
            self.cart[product_id] = int(quantity)

        # Save the session after making changes
        self.session.modified = True

    def __len__(self):
        # Return the number of items in the cart
        return sum(self.cart.values())

    def get_prods(self):
        # Get the products in the cart based on the stored product ids
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        # Return the quantities of products in the cart
        return self.cart

    def update(self, product_id, quantity):
        # Update the quantity of a product in the cart
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id] = int(quantity)

        # Save the session after updating
        self.session.modified = True

    def delete(self, product):
        # Delete a product from the cart
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        # Save the session after deleting
        self.session.modified = True

    def cart_total(self):
        # Calculate the total price of the cart
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    # If the product is on sale, apply sale price
                    if product.is_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value
        return total
