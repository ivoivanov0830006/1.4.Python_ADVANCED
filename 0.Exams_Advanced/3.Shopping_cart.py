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


"""
------------------------------------ Problem to resolve --------------------------------

Write a function called shopping_cart that adds products to a shopping cart for the following 
three types of meals:  "Soup", "Pizza", and "Dessert". Every meal has a limit of products that 
can be added to it:
        Soup: 3
        Pizza: 4
        Dessert: 2
Once you reach the limit of a meal, you should stop adding products to that meal.
The function will receive a different number of arguments. The arguments will be passed as 
tuples with two elements - the first one is the type of meal, and the second is the product 
for the meal. You need to take each argument and make a dictionary with the meal's name as a 
key and the products as a value of the corresponding key.
There are some additional requirements:
If you receive the same product for the same meal more than once, you must not add it again.
If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding 
products to the cart - just sort and return the desired result as described below.
In the end, sort the meals by the number of bought products in descending order. If there are 
meals with an equal number of products, sort them (the meals) by their name in ascending order 
(alphabetically). For each meal sort its products in ascending order (alphabetically).
Return an output as described below.
Note: Submit only the function in the judge system
Input
There will be no input, just parameters passed to your function
Output
Return a string for each of the 3 types of a meal of the sorted result in the format:
        "{meal_type}:"
        " - {first_product_added}"
        " - {second_product_added}"
         …
        " - {Nth_product_added}"
If there are no products given for a meal, return just its name in the format shown above.
If there are NO products in the cart (at all), return the message: 
        "No products in the cart!"
Constrains
Each tuple given will always contain the type of meal in the first position and a product in 
the second. There will be no other meals passed than "Soup", "Pizza", and "Dessert".
-------------------------------------- Example inputs ----------------------------------
Test Code
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))	Pizza:
 - cheese
 - flour
 - ham
 - mushrooms
Output
Dessert:
 - milk
Soup:
 - carrots
--------------------------------
Test Code
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))	
Output
Dessert:
 - milk
Pizza:
 - ham
Soup:
--------------------------------
Test Code
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))	
Output
No products in the cart!

"""
