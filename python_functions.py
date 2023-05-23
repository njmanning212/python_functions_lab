#Challenge 1:

# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

#Solution:

def sum_to(n):
    sum = 0
    for i in range(0, n+1):
        sum = sum+i
    return sum

# print(sum_to(6))
# print(sum_to(10))

# ----------------------------------------------------------------

#Challenge 2:

# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

#Solution:

def largest(list):
    largets_num = list[0]
    for i in list:
        if i > largets_num:
            largets_num = i
    return largets_num

# print (largest([1, 2, 3, 4, 0]))
# print (largest([10, 4, 2, 231, 91, 54]))

# ----------------------------------------------------------------

#Challenge 3:

# Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.


#Solution:

def occurrences(first_string, second_string):
    count = first_string.count(second_string)
    return count

print (occurrences('fleep floop', 'e'))
print (occurrences('fleep floop', 'p'))
print (occurrences('fleep floop', 'ee'))
print (occurrences('fleep floop', 'fe'))