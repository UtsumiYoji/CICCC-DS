from pprint import pprint

def main():
    cart = [
        {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
        {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
        {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
        {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
    ]
    
    # 1
    pprint(cart)

    # 2
    print('\nTotal', sum([v["quantity"]*v["price_per_unit"] for v in cart]), '\n')

    # 3
    cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})

    # 4
    cart[1]["quantity"] = 10
    print(cart, '\n')

    # 5
    del cart[3]
    print(cart)


if __name__ == '__main__':
    main()