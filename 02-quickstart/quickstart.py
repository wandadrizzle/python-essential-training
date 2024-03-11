#Remember to type jupyter notebook in terminal
number_in_algebra = 3j
print(type(number_in_algebra))

print()
my_list = [[1,2,3],[False, True], []]
print("My list of lists has a length of", len(my_list))

print()
print("- random text -" * 4)
print(20//4) #Removes decimal and ultimately makes answer an integer instead of default float
print(3**2) #Exponents => base ^ exponent

#Memebership operators
print(2 in [1, 2, 3, 4,6, 9])

#Print doesn't return anything
print(print("Camp Lazlo!")) #None represents the absence of a value
print()
print("= CHALLENGE =" * 6)

def factorial(number):
    #if not isinstance(number, (int, float)):
    if not isinstance(number, (int)):
        return None  # Return None if the input is not a number
    elif number < 0:
        #return None
        return "You can't get a factorial of a negative number."
    elif number == 0:
        return "The factorial of 0 is 1, this is also known as the base case"
    else:
        answer = 1
        for i in range(1, number + 1):
            answer *= i
        return "The factorial of " + str(number) + " is " + str(answer) + "."
    

print(factorial("spam"))
print(factorial(4.5))
print("Negative number factorial")
print(factorial(-36))
print("Factorial of zero")
print(factorial(0))
print("Positive number factorial")
print(factorial(9))
print(456%10)

var = (1,2,3)
#var.append(4)

'''
a = [1,2,3,4]
while True:
    print(a[0])

'''