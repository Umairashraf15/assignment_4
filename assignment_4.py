def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
# Getting user name
    name = input("Enter your name: ")
    
# Collecting favorite numbers
    num1 = int(input("Enter your 1st favorite number: "))
    num2 = int(input("Enter your 2nd favorite number: "))
    num3 = int(input("Enter your 3rd favorite number: "))
    
# Greeting the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    
# Checking if the numbers are even or odd
    if num1 % 2 == 0:
        print(f"The number {num1} is even.")
    else:
        print(f"The number {num1} is odd.")
        
    if num2 % 2 == 0:
        print(f"The number {num2} is even.")
    else:
        print(f"The number {num2} is odd.")
        
    if num3 % 2 == 0:
        print(f"The number {num3} is even.")
    else:
        print(f"The number {num3} is odd.")
    
# Calculating and displaying squares
    print("\nLet's look at the squares of your numbers:")
    print(f"The number {num1} and its square: ({num1}, {num1 ** 2})")
    print(f"The number {num2} and its square: ({num2}, {num2 ** 2})")
    print(f"The number {num3} and its square: ({num3}, {num3 ** 2})")
    
# Calculating sum of numbers
    total = num1 + num2 + num3
    print(f"\nAmazing! The sum of your favorite numbers is: {total}")
    
# Checking if sum is prime
    if is_prime(total):
        print(f"Wow, {total} is a prime number!")
    else:
        print(f"{total} is not a prime number, but it's still awesome!")

if __name__ == "__main__":
    main()
