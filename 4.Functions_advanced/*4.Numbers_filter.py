def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = list(filter(lambda x: x % 2 != 0, kwargs["odd"]))

    if "even" in kwargs:
        kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))

    return {key: value for key, value in sorted(kwargs.items(), key=lambda x: -len(x[1]))}


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))


"""
------------------------------------- Another Solution ---------------------------------

def even_odd_filter(**kwargs):
    result = {}
    if "odd" in kwargs:
        kwargs["odd"] = [n for n in kwargs["odd"] if n % 2 == 1]
    if "even" in kwargs:
        kwargs["even"] = [n for n in kwargs["even"] if n % 2 == 0]
    
    return {key: value for key, value in sorted(kwargs.items(), key=lambda x: -len(x[1]))}
        
        
print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))


------------------------------------- Another Solution ---------------------------------

def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        checking = 0 if key == "even" else 1
        filtered = [x for x in value if x % 2 == checking]
        result[key] = filtered

    return {key: value for key, value in sorted(result.items(), key=lambda x: -len(x[1]))}
    # -len(x[1]) is giving descending order


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))


------------------------------------ Problem to resolve --------------------------------

Create a function called even_odd_filter() that can receive a different number of named arguments. The keys 
will be "even" and/or "odd", and the values will be a list of numbers.  
When the key is "odd", you should extract only the odd numbers from its list. When the key is "even", you 
should extract only the even numbers from its list.
The function should return a dictionary sorted by the length of the lists in descending order. There will 
be no case of lists with the same length.
-------------------------------------- Example inputs ----------------------------------
Input	
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))	
Output
{'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}
-------------------------------------------
Input	
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))	
Output
{'odd': [5]}

"""
