def is_palindrome_number(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

num = int(input("Enter a number: "))
is_palindrome_number(num)