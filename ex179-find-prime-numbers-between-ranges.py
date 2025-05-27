def find_prime_numbers(start, to):
    prime_numbers = []
    for x in range(start, to):
        is_prime = True
        y = 2
        while (y < x and is_prime):
            if x % y == 0:
                is_prime = False
            else:
                y += 1
        if is_prime:
            prime_numbers.append(x)
    print(prime_numbers)

find_prime_numbers(10,50)

