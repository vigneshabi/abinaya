list1 = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    list1.append(numbers)
print("Maximum element in the list is :", max(list1), "\nMinimum element in the list is :", min(list1))

