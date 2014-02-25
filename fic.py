__author__ = 'souriyakhaosanga'

#Time efficiency is big O(mn)
#Method is used to find mutual friends
def brute_force(array1, array2):
    mutual = []
    for i in array1:
        for j in array2:
            if i == j:
                mutual.append(i)
    print mutual

#
#Friends in common log n
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

    person1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    person2 = [2, 5, 7, 8, 9]

    brute_force(person1, person2)

    faster(person1, person2)


if __name__ == "__main__":
    main()