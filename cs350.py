#Souriya Khaosanga

import itertools
import collections

#Build the list of permutations using lexigraphic
def build_list(input_string):
    my_list = list()
    for c in itertools.combinations(list(input_string), input_string.__len__()):
        for p in itertools.permutations(c):
            string = "".join(p)
            my_list.append(string)

    return my_list

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def print_index(list):
    print list[1]

def duplicate(list):
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

    print "-----------Number of n list--------"
    print input_list.__len__()
    print test.__len__()

    #sort the input_list here lexigraphically
    sorted_list = sorted(input_list)

    print "-------Comparing the two list after sorting-------"
    if collections.Counter(input_list) == collections.Counter(sorted_list):
        print "sorted lexigraphically"

if ( __name__ == "__main__" ):
    main()



