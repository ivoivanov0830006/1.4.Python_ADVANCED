def shopping_list(budget, **needed_items):
    if budget >= 100:
        bought_products = {}
        for product, info in needed_items.items():
            value, quantity = info[0], info[1]
            current_total = value * quantity
            if budget >= current_total:
                budget -= current_total
                if product not in bought_products.keys():
                    bought_products[product] = 0
                bought_products[product] += current_total
            if len(bought_products) == 5:
                break

        final_string = ""
        for key, value in bought_products.items():
            final_string += f"You bought {key} for {value:.2f} leva.\n"

        return final_string

    return "You do not have enough budget."


print(shopping_list(110,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
