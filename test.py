class Person:

    def __description(self):
        return "Person function"

    def printInfo(self):
        print self.__description()


class Parent(Person):
    def __description(self):
        return "Parent function"
    def printInfo(self):
        print self.__description()


def main():
    a = Person()
    b = Parent()
    a.printInfo()
    b.printInfo()

if __name__ == "__main__":
    main()