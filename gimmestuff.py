__author__ = 'souriyakhaosanga'


class Employee:
    numOfEmployee = 0

    def __init__(self, nameOfEmployee, ageOfEmployee):
        self.name = nameOfEmployee
        self.age = ageOfEmployee
        Employee.numOfEmployee += 1

    def displayCount(self):
        print self.numOfEmployee

    def displayEmp(self):
        print self.name
        print self.age


def main():
    emp1 = Employee("rick", 25)
    emp2 = Employee("sean", 95)
    emp3 = Employee("leloc", 54)

    print dir(emp1)


if __name__ == "__main__":
    main()