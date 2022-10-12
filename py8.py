def palindrome(number):
    print("Original number", number)
    original_num = number

    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10 + reminder)
        number = number // 10

    if original_num == reverse_num:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")


palindrome(121)
palindrome(125)
palindrome(100001)
palindrome(55555)
