while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue 

    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a valid second number.")
        continue 

    else:
        print(f"Result: {num1} ÷ {num2} = {result}")
        break
