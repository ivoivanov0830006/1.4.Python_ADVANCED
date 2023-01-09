def find_sums(*args):
    positive_sum = 0
    negative_sum = 0
    for element in args:
        if element > 0:
            positive_sum += element
        else:
            negative_sum += element

    return positive_sum, negative_sum


numbers = [int(x) for x in input().split()]

positive_sum, negative_sum = find_sums(*numbers)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
