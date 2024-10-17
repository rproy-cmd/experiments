def factorial(n):
    if not isinstance(n,int):
        return "Input must be of integer value"
    if n<0:
        return "Factorial cannot be generated for negative values"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    num = 5  # You can change this value to test with other numbers
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

if __name__ == "__main__":
    main()
