import random

__author__ = 'souriyakhaosanga'

def dutch_national_flag(arrayInput, length):
    high = length - 1
    p = 0
    i = 0
    while i <= high:
        if arrayInput[i] == 0:
            #swap
            arrayInput[i], arrayInput[p] = arrayInput[p], arrayInput[i]
            p += 1
            i += 1
        elif arrayInput[i] == 2:
            #swap
            arrayInput[i], arrayInput[high] = arrayInput[high], arrayInput[i]
            high -= 1
        else:
            i += 1


def main():
    #create a stack of random numbers
    stack = []
    i = 0
    while i <= 35:
        stack.append(random.randint(0, 2))
        i += 1

    print "Input: ", stack
    dutch_national_flag(stack, len(stack))
    print "Sorted: ", stack

if __name__ == "__main__":
    main()