class Calculator:
    sum2 = 0
    def __init__(self,num):
        self.num1 = num

    def sum(self):

        for i in self.num1:
            self.sum2+=i
        return self.sum2

    def avg(self):
        self.sum3=self.sum2/len(self.num1)
        return  self.sum3

if __name__ == "__main__":
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())
    cal2 = Calculator([6,7,8,9,10])
    print(cal2.sum())
    print(cal2.avg())



