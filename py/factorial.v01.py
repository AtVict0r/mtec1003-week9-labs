def factorial(n):
    total = 1

    for i in range(n):
        total *= (n-i)
        print("Current i: " + str(i) + ", Current total: " + str(total))

    return total # Return final value of total at the end of the loop

factorialNumber = int(input("Enter a number to find its factorial: "))
result = factorial(factorialNumber)
print("Factorial of", factorialNumber, "is", result)
