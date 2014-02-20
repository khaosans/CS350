__author__ = 'souriyakhaosanga'

#Method is used to find mutual friends
def brute_force(array1, array2):
    mutual = []
    for i in array1:
        for j in array2:
            if i == j:
                mutual.append(i)
    print mutual



def main():
    print "program for mutual friends"

    person1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    person2 = [2, 5, 7, 8, 9]

    brute_force(person1, person2)




if __name__ == "__main__":
    main()