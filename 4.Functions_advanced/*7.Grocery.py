def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (x-[1], -len(x[0]), x[0]))
    result = []

    for product, quantity in kwargs:
        result.append(f"{product}: {quantity}")

    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


"""
------------------------------------- Another Solution ---------------------------------

def grocery_store(**kwargs):
    sorted_result = [f"{key}: {value}" for key, value in sorted(kwargs.items(), key=lambda x:
                (-x[1], -len(x[0]), x[0]))]   # value, length, alphabetically
    return "\n".join(sorted_result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


------------------------------------ Problem to resolve --------------------------------

Create a function called grocery_store() that receives a different number of key-value pairs. The key will 
be the product's name and the value - its quantity. 
You should return a sorted receipt for all products. They should be sorted by their quantity in descending 
order. If there are two or more products with the same quantity, sort them by their name's length in 
descending order. If there are two or more products with the same name's length, sort them by their name in
 ascending order (alphabetically). In the end, return a string in the following format:
       "{product_name1}: {product_quantity1}
        {product_name2}: {product_quantity2}
         …       
        {product_nameN}: {product_quantityN}"
-------------------------------------- Example inputs ----------------------------------
Test Code	
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))	
Output
pasta: 12
eggs: 12
bread: 5
-------------------------
Test Code
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))	
Output
eggs: 20
bread: 2
pasta: 2
carrot: 1

"""
