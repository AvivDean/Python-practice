number = int(input("Enter a number to reverse "))

print("Given number is: ", number)
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")
