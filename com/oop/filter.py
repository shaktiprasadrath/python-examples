class Filter:

    def __init__(self):
        self.blank=[]

    def filter_demo(self, seq):
        return [x for x in seq if x not in self.blank]

    def display(self):
        val = Filter()
        y = val.filter_demo([1, 2, 3, 4, 5])
        print(list(y))


f = Filter().display()


#if __name__== '__main__':
#    Filter().display()