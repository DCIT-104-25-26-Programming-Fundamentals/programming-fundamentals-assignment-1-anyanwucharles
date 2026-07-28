# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def generate_fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]

sequence = [0, 1]
while len(sequence)< n:
  sequence.append(sequence[-1] + sequence[-2])
  return sequence

def is_fibonacci(num):
  if num < 0:
    return False
    a, b = 0, 1
    while a < num
a, b = b, a + b
return a == num

def part_a():
  n_input = input("How many terms? ")
  try:
    n = int(n_input)
    if n<= 0:
      print("Error: N must be a positive integer.")
    else:
      fib_list = generate_fibonacci(n)
      print("Fibonacci sequence:", " ".join(str(x) for x in fib_list))
  except ValueError:
    print("Error: N must be a positive integer.")

part_b():
num_input = input("Enter a number to check: ")
try:
  num = int(num_input)
  if is_Fibonacci(num):
    print(f"{num} is a Fibonacci number.")
  else:
    print(f"{num is NOT a fibonacci number.")
except ValueError:
  print("Please enter a valid integer.")

part_a()
part_b()
 
