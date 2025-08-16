# Task 1: Function to add two numbers
def add_numbers(n1, n2):
    return n1 + n2

# Example for Task 1
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("The sum is", add_numbers(n1, n2))


# Task 2: Function to calculate square of a number
def square(num):
    return num * num

# Example for Task 2
num = int(input("\nEnter a number: "))
print(f"Square of {num} is {square(num)}")


# Task 3: Function to calculate bill with tax
def calculate_bill(items, tax_rate=0.08):
    subtotal = sum(items)
    total = subtotal + (subtotal * tax_rate)
    return total

# Example for Task 3
items = [100, 200, 50]
print("\nTotal bill after tax: $", calculate_bill(items))


# Task 4: Function to generate bill receipt
def generate_bill(items, prices):
    total = 0
    print("\n----- Bill Receipt -----")
    for i in range(len(items)):
        print(f"{items[i]} - ${prices[i]}")
        total += prices[i]
    print("Total: $", total)

# Example for Task 4
items = ["Apple", "Milk", "Bread"]
prices = [2, 3, 1]
generate_bill(items, prices)

print("\nKeep Coding and Keep Smiling! 😊")
