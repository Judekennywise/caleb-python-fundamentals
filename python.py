even_count = 0
odd_count = 0
for number in range(1, 31):
    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("even count = "+ str(even_count))
print("odd_count =" + str(odd_count))
