def palindrome(word, idx):
    if idx >= len(word) // 2:
        return f"{word} is palindrome"

    left = word[idx]
    right = word[-1 - idx]
    if left != right:
        return f"{word} is not palindrome"

    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))


"""

------------------------------------- Another Solution ---------------------------------

word = "abcba"
for idx in range(len(word) // 2):
    left = word[idx]
    right = word[-1 - idx]
    if left != right:
        print(f"{word} is not palindrome")
        break

else:
    print(f"{word} is palindrome")


------------------------------------ Problem to resolve --------------------------------

Write a recursive function called palindrome() that will receive a word and an index (always 0). 
Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} 
is not a palindrome" if the word is not a palindrome using recursion. 
-------------------------------------- Example inputs ----------------------------------
Test Code	
print(palindrome("abcba", 0))	
Output
abcba is a palindrome
---------------------------------
Test Code	
print(palindrome("peter", 0))
Output
peter is not a palindrome

"""
    
