#Souriya Khaosanga

import itertools
import collections

#Build the list of permutations using lexigraphic sorting
def build_list(input_string):
    my_list = list()
    for c in itertools.combinations(list(input_string), input_string.__len__()):
        for p in itertools.permutations(c):
            string = "".join(p)
            my_list.append(string)

    return my_list


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def print_index(list):
    print list[1]


def duplicate(listt):
    seen = set()
    for x in list:
        if x in seen:
            return True
            seen.add(x)
    return False


def array_equal(array1, array2):
    for x in array1:
        if array1[x] != array2[x]:
            print "not equal"

#Check for permutation of any letter input
def main():

    test = [''.join(i) for i in itertools.permutations("abcdefghij")]

    input_list = build_list("abcdefghij")

    #checks the input_list for duplicates

    if not duplicate(input_list):
        print "No duplicates Exist"

    if not duplicate(test):
        print "No duplicates Exist"

    print input_list.__len__()
    print test.__len__()

    #sort the input_list here lexigraphically
    sorted_list = sorted(input_list)

    if collections.Counter(input_list) == collections.Counter(sorted_list):
        print "sorted lexigraphically"


if ( __name__ == "__main__" ):
    main()



