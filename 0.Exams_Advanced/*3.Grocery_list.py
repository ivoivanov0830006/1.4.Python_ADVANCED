def shop_from_grocery_list(budget, product_list, *args):

    for data in args:
        product = data[0]
        price = float(data[1])
        if product in product_list:
            if budget < price:
                break
            elif budget >= price:
                budget -= price
                product_list.remove(product)

    if product_list:
        return f"You did not buy all the products. Missing products: {', '.join(product_list)}."

    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
