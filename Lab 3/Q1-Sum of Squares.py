# Omer Mustafa - F2016-472
# Artificial Intelligence by Dr. Iftikhar Hussain
# Lab no. 3 - Question no.1
# Write a python program to calculate the sum of squares in given digit. Program accepts a
# positive number as input and calculates the sum of squares of individual digits of the given
# number.



# Return the sum of 
# square of first n 
# natural numbers 
def squaresum(n) : 
  
    # Iterate i from 1  
    # and n finding  
    # square of i and 
    # add to sum. 
    sm = 0
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
      
    return sm 
  
# Driven Program 
n = int(input("Enter your number"))
print(squaresum(n)) 
  