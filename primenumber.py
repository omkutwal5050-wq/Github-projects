def is_prime(n):
    if n <= 1:
        print("Not Prime")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")

num = int(input("Enter a number: "))
is_prime(num)