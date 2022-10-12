getNumber = input()
if int(getNumber) < 10:
    print("enter a number greater than or equal to 10")
    getNumber = input()
temp = int(getNumber) - 10
print("Printing current and previous number sum in a range of " + str(temp) + "-" + str(getNumber))
for number in range(10):
    print("Current number is ", temp+1, " previous number is: ", temp, " The Sum is: ", temp+temp+1)
    number = number+1
    temp = temp+1
