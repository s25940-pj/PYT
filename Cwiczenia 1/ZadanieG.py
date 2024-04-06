def is_palindrome(word):
    return word == word[::-1]


word = input("Podaj słowo: ")
print(is_palindrome(word))
