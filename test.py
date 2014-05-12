



class Parent(object):
    def __init__(self):
        pass
    def Create(self):
        return 'someshit here'

class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        self.Create()
    def Create(self):
        return 'the'+super(Child,self).Create()

def main():

    print Child().Create()

if __name__ == "__main__":
    main()