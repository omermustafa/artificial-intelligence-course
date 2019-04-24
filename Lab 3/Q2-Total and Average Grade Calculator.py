# Omer Mustafa - F2016-472
# Artificial Intelligence by Dr. Iftikhar Hussain
# Lab no. 3 - Question no.2
# Write a program that allows the user to a series of numerical grades and then calculates an
# average. Entering an integer of value 0 ends the input and produces the result. Use two separate
# functions (methods) to 1) input data and calculate the total of all grades entered and 2) calculate
# the average.

def calculateAverage(sum, values):
    return sum / (values-1)

def gradeCalculator():
    print("Input some integers to calculate their sum and average. Input 0 to exit.")

    count = 0
    sum = 0.0
    number = 1

    while number != 0:
        number = int(input(""))
        sum = sum + number
        count += 1

    if count == 0:
        print("Input some numbers")
    else:
        print("Average and Sum of the above numbers are: ", calculateAverage(sum, count), sum)


#Driver Function
gradeCalculator()
