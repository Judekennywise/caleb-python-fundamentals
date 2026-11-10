# # for number in range(1,21):
#     if number % 3 == 0:
#        print(number)
# WARM-UP 1


# div_count = 0
# notdiv_count = 0
# for number in range(1,51):
#     if number % 5 == 0:
#         div_count = div_count + 1
#     else: notdiv_count = notdiv_count + 1
# print("The numbers divisible by 5 are:" , div_count)  
# WARM-UP 2 

secret_number = 8
att_count = 0
for attempt in range(3):
   att_count = att_count + 1
   print("Attempt " + str(att_count ) + " of 3")
   guess = int(input("Guess a number between 1 and 10: "))

   if guess == secret_number:
    print("You guessed the correct number!")
    break
   elif guess > secret_number:
    print("Too high!")
   else:
    print("Too low!")   
else:    
    print("Game over. The secret number was " + str(secret_number) + ".")     

print("You used " + str(att_count) + " attempts.") 




