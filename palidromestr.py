def is_palindrome_string(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

string = input("Enter a string: ")
is_palindrome_string(string)