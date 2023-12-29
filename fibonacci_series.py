def generate_fibonacci(n):
    # Adding comment 
    # REmoved a few comments and added a few
    # Added additional comments

    fib_series = [0, 1]
    print(fib_series)

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series[:n]

# Example: Generate the first 10 Fibonacci numbers
n = 10
fibonacci_series = generate_fibonacci(n)
print(f"Fibonacci Series (first {n} numbers): {fibonacci_series}")

def dummy_function():
    print("It is a dummy funtion.")