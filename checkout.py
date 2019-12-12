import re
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
        for index , digit in digits:
            if(index%2==0):
                double.append(digit*2)
            else:
                double.append(digit)

        double = [self.sumdig(x) for x in double]
        sumOfDigits = sum(double)
        return sumOfDigits%10==0

    def cvv(self,cvv_number):
        cv = str(cvv_number)
        if(len(cv)==3):
            return True
        else:
            return False

    def expiryDate(self,month,year):
        if(month<=12 and month>=1 and year>2019):
            return True
        else:
            return False

