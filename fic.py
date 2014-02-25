__author__ = 'souriyakhaosanga'

#This is problem number #2



#Time efficiency is big O(mn)
#Method is used to find mutual friends
#This pretty much just compares each index in
#the array1 to each index of array2.
#It is actually pretty slow compare to the 2nd faster
#method
def brute_force(array1, array2):
    mutual = []
    for i in array1:
        for j in array2:
            if i == j:
                mutual.append(i)
    print mutual

#
#The time efficiency of this function is O(n log n)
#The method is much faster as that it uses 4 arrays
#The array1 is concatenated directly onto the array2
#which is called array c
#Afterwhich, c is sorted.  Python has a built in
#sort called tim sort. Cited here http://en.wikipedia.org/wiki/Timsort
#Then after each index in the sorted array is compared to it's
#adjacent member in the array.  If there is a match, it is saved
#and copied over to the d array--this is the in commons array.
def faster(array1, array2):
    c = []
    d = []
    c += array1
    c += array2
    c.sort()
    for i in range(0, c.__len__() - 1, 1):
        if c[i] == c[i + 1]:
            d.append(c[i])
    print d


def main():
    print "program for mutual friends"

    person1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    person2 = [2, 5, 7, 8, 9, 3]
    print "input 1: ", person1
    print "input 2: ", person2

    print "Brute force: "
    brute_force(person1, person2)
    print "None brute: "
    faster(person1, person2)


if __name__ == "__main__":
    main()