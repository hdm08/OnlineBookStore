from django import template
register =template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(book,cart):
    keys=cart.keys()
    for id in keys:
        # print(type(id),type(book.id))
        if id==str(book.id):
            return True
    return False




@register.filter(name='cart_quantity')
def cart_quantity(book,cart):
    keys=cart.keys()
    for id in keys:
        # print(type(id),type(book.id))
        if id==str(book.id):
            return cart.get(id)
    return 0



@register.filter(name='price_total')
def price_total(book, cart):
    return int(book.price) * int(cart_quantity(book,cart))


@register.filter(name='total_cart_price')
def total_cart_price(book, cart):
    sum = 0
    for b in book:
        sum += price_total(b, cart)

    return sum


@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)



@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1
