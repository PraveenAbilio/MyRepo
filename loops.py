def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def main():
    n = int(input("Enter the number of terms for Fibonacci sequence: "))
    
    result = fibonacci(n)
    print(f"Fibonacci sequence up to {n} terms: {result}")

if __name__ == "__main__":
    main()


