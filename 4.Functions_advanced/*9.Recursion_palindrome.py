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
    
    
