def words_sorting(*args):
    all_words = {}
    result = ""
    total_sum = 0

    for word in args:
        word_sum = sum(ord(letter) for letter in word)
        if word not in all_words:
            all_words[word] = 0
        all_words[word] = word_sum
        total_sum += word_sum

    if total_sum % 2 == 0:
        sorted_all_words = sorted(all_words.items(), key=lambda x: x[0])
    else:
        sorted_all_words = sorted(all_words.items(), key=lambda x: x[1], reverse=True)

    for key, value in sorted_all_words:
        result += f"{key} - {value}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))


"""
------------------------------------ Problem to resolve --------------------------------

Write a function words_sorting which receives a different number of words.
Create a dictionary, which will have as keys the words that the function received. For each key, create a 
value that is the sum of all ASCII values of that key. Then, sort the dictionary:
    * By values in descending order, if the sum of all values of the dictionary is odd
    * By keys in ascending order, if the sum of all values of the dictionary is even
Input
There will be no input, just any number of words passed to your function
Output
The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
Constraints:
There will be no case with capital letters.
There will be no case with a string consisting of other than letters.
