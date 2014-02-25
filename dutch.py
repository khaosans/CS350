#Problem #4
#Random is used for testing the program
import random

__author__ = 'souriyakhaosanga'

#This method is pretty much sorting the array.
#
def dutch_national_flag(arrayInput):
    maxOfArray = arrayInput.__len__() - 1
    p = 0
    i = 0
    while i <= maxOfArray:
        if arrayInput[i] == 0:
            #Perform Swap of the array indexes
            arrayInput[i], arrayInput[p] = arrayInput[p], arrayInput[i]
            p += 1
            i += 1
        elif arrayInput[i] == 2:
            #Perform swap of the array indexes
            arrayInput[i], arrayInput[maxOfArray] = arrayInput[maxOfArray], arrayInput[i]
            maxOfArray -= 1
        else:
            i += 1

#Method is used for building array of random colors of the
#dutch national flag
def build_random_array(size):
    stack = []
    i = 0
    while i <= size:
        #create random numbers between 0-2 to simulate the three colors
        #of the ducth national flag
        stack.append(random.randint(0, 2))
        i += 1
    return stack

def print_test(stack):
    print "input: ", stack
    dutch_national_flag(stack)
    print "after: ", stack


def main():

    print "Test 1"
    stack = build_random_array(40)
    print_test(stack)

    print "Test 2"
    stack1 = build_random_array(10)
    print_test(stack1)

    print "Test 3"
    stack2 = build_random_array(5)
    print_test(stack2)

if __name__ == "__main__":
    main()