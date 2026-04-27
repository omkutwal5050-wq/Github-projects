while True:
    print("\nMENU")
    print("1. Arithmetic operation")
    print("2. Relational operation")
    print("3. Logical operation")
    print("4. Assignment operation")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    # 🔢 Arithmetic
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)
        if b != 0:
            print("Division:", a / b)
        else:
            print("Division not possible")

    # 🔍 Relational
    elif choice == 2:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("x > y :", x > y)
        print("x < y :", x < y)
        print("x == y :", x == y)
        print("x != y :", x != y)
        print("x >= y :", x >= y)
        print("x <= y :", x <= y)

    # 🔗 Logical
    elif choice == 3:
        p = bool(int(input("Enter first value (0/1): ")))
        q = bool(int(input("Enter second value (0/1): ")))
        print("AND:", p and q)
        print("OR:", p or q)
        print("NOT p:", not p)
        print("NOT q:", not q)

    # 📌 Assignment
    elif choice == 4:
        a = int(input("Enter a number: "))
        print("Original value:", a)
        a += 5
        print("After +=5:", a)
        a -= 3
        print("After -=3:", a)
        a *= 2
        print("After *=2:", a)
        a /= 2
        print("After /=2:", a)

    # ❌ Exit
    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")