#Challenge 1:

# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

#Solution:

def sum_to(n):
    sum = 0
    for i in range(0, n+1):
        sum = sum+i
    return sum

print(sum_to(6))
print(sum_to(10))