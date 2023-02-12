def shopping_cart(*args):
    order = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }

    limit = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
        }

    for data in args:
        final_result = ""
        if data == "Stop":
            if not order["Soup"] and not order["Pizza"] and not order["Dessert"]:
                return "No products in the cart!"
            sorted_result = sorted(order.items(), key=lambda x: (-len(x[1]), x[0]))

            for key, value in sorted_result:
                final_result += f"{key}:\n"
                sorted_products = sorted(value)
                for product in sorted_products:
                    final_result += f" - {product}\n"
            return final_result

        meal = data[0]
        ingredient = data[1]

        for type_meal, count_ingredient in limit.items():
            if type_meal == meal:
                if meal not in order.keys():
                    order[meal] = []
                if limit[type_meal] != 0 and ingredient not in order[meal]:
                    order[meal].append(ingredient)
                    limit[meal] -= 1


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
