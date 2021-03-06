

# Simple Sum method

def sum(num1, num2):
    print(num1 + num2)


sum(7, 8)           
sum("Devops", 5)                    # Will produce an unexpected behaviour

# Type hinting

def sum_with_hint(num1: int, num2: int) -> int:
    print(num1 + num2)

sum_with_hint(4, 5)