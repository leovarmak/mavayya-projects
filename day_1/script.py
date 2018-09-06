import random

array = []  # Initializing a random array
counter = 0

while counter < 100:
    array = array + [random.randint(0,9)]   # Inserting a new element into the array
    counter = counter + 1   # Incrementing the counter 

print array

for i in range(len(array)):
    for j in range(0, len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print ("Sorted array is:")
print array

