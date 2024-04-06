def is_even(n: int) -> bool:
    try:
        n = int(n)
    except ValueError:
        print("Podana wartość nie jest liczbą całkowitą")
        exit(1)
    return n % 2 == 0


n = input("Podaj liczbę całkowitą: ")
print(is_even(n))
