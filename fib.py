def fibonacci_series(n):
  fib_series = [0, 1]
  for i in range(2, n):
    fib_series.append(fib_series[i-1] + fib_series[i-2])
  return fib_series
  
def is_palindrome(number):
  return str(number) == str(number)[::-1]
  
# User input
num_terms = int(input("Enter the number of terms for Fibonacci series: "))
fib_series = fibonacci_series(num_terms)
print("Fibonacci Series:", fib_series)
num_to_check = int(input("Enter a number to check if it is a palindrome: "))
if is_palindrome(num_to_check):
  print(f"{num_to_check} is a palindrome number.")
else:
  print(f"{num_to_check} is not a palindrome number.")
