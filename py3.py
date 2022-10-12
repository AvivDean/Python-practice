def remove_chars(word,n):
    x = word[n:]
    return x


print("Removing characters from string")
n = int(input("Enter a number "))
print("removing all chars until the ", n, " in the string: 'Aviv is Negev's father' : ",
      remove_chars("Aviv is Negev's father", n))
