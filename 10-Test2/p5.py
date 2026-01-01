cart = {'juice':4,'bread':1,"milk":2}
prices = {'milk':1.49,'butter':2.09,'juice':1.19,'bread':1.99}
def f(shopping_cart,price_list,customer_wallet):
    sum =0
    for product,price in shopping_cart.items():
        sum += shopping_cart[product] * price_list[product]
    if sum > customer_wallet:
        return False
    else:
        return True
if __name__ == "__main__":
    print(f(cart,prices,10))
    print(f(cart,prices,8))