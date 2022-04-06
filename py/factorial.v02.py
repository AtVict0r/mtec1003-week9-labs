def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

factorialNumber = int(input("Enter a number to find its factorial: "))
result = factorial(factorialNumber)
print("Factorial of", factorialNumber, "is", result)