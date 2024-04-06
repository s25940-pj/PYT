fruits = ["jabłko", "gruszka", "banan", "pomarańcza", "banan", "jabłko"]

# 1. Wypisz zawartość listy słów
print(fruits)

# 2. Znajdź liczbę słów w liście
print(len(fruits))

# 3. Posortuj zawartość listy (słowa) alfabetycznie
fruits.sort()
print(fruits)

# 4. Znajdź ilość wystąpień każdego słowa w liście
for fruit in set(fruits):
    print(fruit, fruits.count(fruit))
