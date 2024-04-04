from market.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def total_price(self):
        total = 0
        for product_id, product_info in self.cart.items():
            total += int(product_info['price'])
        return total

    def filter_product(self):
        product_ids = self.cart.keys()
        product = Product.objects.filter(id__in=product_ids)
        return product

    def remove(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
