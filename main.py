first = int(input("First: "))
second = int(input("Second: "))

request = input("Add, Divide, Multiply, or Subtract?: ")

if request.lower() == "add":
    sum = first + second
    print("Sum is: " + str(sum))

elif request.lower() == "divide":
    if first != 0:
        divided = first/second
        print("The result of the divide is: " + str(divided))

elif request.lower() == "multiply":
    if first and second != 0:
        multiplied = first * second
        print("The result of the multiplication is: " + str(multiplied))

elif request.lower() == "subtract":
    subtraction: first - second
    print("The result of the subtraction is: " + str(subtraction))

else:
    print("One, or both of the numbers you have input are not compatible")