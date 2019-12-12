class Ticket:

    def setChildTicketPrice(self,child):
        self.child = child

    def getChildTicketPrice(self):
        return self.child

    def setAdultTicketPrice(self,adult ):
        self.adult = adult

    def getAdultTicketPrice(self):
        return self.adult

    def setSeniorTicketPrice(self, senior):
        self.senior = senior

    def getSeniorTicketPrice(self):
        return self.senior

    def setConcessionTicketPrice(self,concession):
        self.concession = concession

    def getConcessionTicketPrice(self):
        return self.concession

    def setTotal(self,total):
        self.total = total


    def getTotal(self):
        return self.total