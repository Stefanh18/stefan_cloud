# The program generates prints out the sum of previos 3 numbers starting at number 1
# If there are less than 3 number before the output it prints out the sum of them
# the program prints out the sequence 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

n = int(input("Enter the length of the sequence: ")) # Do not change this line
sum_of_int = 0
counter = 0
for x in range(1, n+1):
    if x <= 3:
        sum_of_int = x
    else:
        sum_of_int = sum_of_int * 2 - counter
        counter += 1
    print(sum_of_int)