import re
pattern = '^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})$'
class Checkout:

    def setCreditCardNumber(self,no):
        self.no = no

    def getCreditCardNumber(self):
        return self.no

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name


    def sumdig(self,digits):
        if(digits<10):
            return digits
        else:
            sum = (digits%10) + (digits//10)
            return sum

    def isValid(self,no):
        no = str(no)
        no = no[::-1]
        no = [int(x) for x in no]
        double = list()
        digits = list(enumerate(no,start=1))
        for ind , digit in digits:
            if(ind%2==0):
                double.append(digit*2)
            else:
                double.append(digit)

        double = [self.sumdig(x) for x in double]
        sumofdigits = sum(double)
        return sumofdigits%10==0







