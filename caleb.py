age=int(input("How old are you? "))
if age > 40:
    print("You are old")
elif age == 35:
    print("Go and marry")
else:
    print("You are young")




user_input = int(input("Type in any number from 1 to 10: "))
odd_numbers = {1,3,5,7,9}
even_numbers = {2,4,6,8,10}
if user_input in odd_numbers:
    print("Your number is an odd number")
else: 
    print("Your number is an even number")