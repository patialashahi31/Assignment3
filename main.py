child = []
adult = []
senior = []

from ticket import Ticket
from checkout import Checkout

h = Ticket()
h.setSeniorTicketPrice(15)
h.setChildTicketPrice(10)
h.setAdultTicketPrice(20)

def messagefirst():
    for j in range(0,5):
        for i in range(0,5):
           if(i<=j):
               print("*",end="")

        print("")

def messagelast():
    for j in range(0,5):
        for i in range(0,5):
           if(j<=i):
               print("*",end="")

        print("")


def message():
    print()
    print()
    print("Ticket Sales")
    #name of program developer print()
    # student id print()
    print("Federation University Australia Robot wars Tickets")
    print()


def menu():
    number_of_senior_tickets = 0
    number_of_adult_tickets = 0
    number_of_child_tickets =0
    print("Type of Tickets")
    print()
    print("1. Child")
    print("2. Adult")
    print("3. Senior citizen")
    print("4. Checkout")
    n = int(input())
    a = [1,2,3,4]
    while(n in a):
        if(n==1):
            child.append(1)
            print("Child ticket added")
            print("Select more tickets")
            n = int(input())
        elif (n==2):
            adult.append(1)
            print("Adult ticket added")
            print("Add more tickets")
            n = int(input())
        elif(n==3):
            senior.append(1)
            print("Senior ticket added")
            print("Add more tickets")
            n = int(input())
        elif(n==4):
            bill()
            break
        else:
            print("Please enter valid number")
            menu()



def bill():
    print("You bought")
    print("Price of "  + str(len(child)) + " child tickets " + " : " + str(h.getChildTicketPrice()) +
          " * " + str(len(child)) + " = " + str(h.getChildTicketPrice()*len(child)) + " dollars")
    print("Price of " + str(len(adult)) + " Adult tickets " + " : " + str(h.getAdultTicketPrice()) +
          " * " + str(len(adult)) + " = " + str(h.getAdultTicketPrice() * len(adult)) + " dollars")
    print("Price of " + str(len(senior)) + " senior tickets " + " : " + str(h.getSeniorTicketPrice()) +
          " * " + str(len(senior)) + " = " + str(h.getSeniorTicketPrice() * len(senior)) + " dollars")
    print("")
    print("Total : " + str(len(child)*h.getChildTicketPrice() +
                           len(adult)*h.getAdultTicketPrice()+
                           len(senior)*h.getAdultTicketPrice()) + " dollars" )
    print()
    print("Press 1 to Checkout")
    n = int(input())
    a = [1]
    while(n in a):
        if (n==1):
            payment()
            break;


check = Checkout()


def payment():
    transactionId=0;
    print("Enter credit card details: ")
    print("Enter name(As on credit card) : " )
    name = input()
    check.setName(name)
    print("Enter credit card number")
    card_number = int(input())
    check.setCreditCardNumber(card_number)
    if(check.isValid(card_number)):
        print("Payment successful")
        transactionId = transactionId + 1
        print("Your unique transaction Id number :" + str(transactionId))
        file1 = open("transactions.txt","w")
        l = [str(transactionId) + " " + check.getName() + " " + str(check.getCreditCardNumber())]
        file1.writelines(l)
        file1.close()
    else:
        print("Card number is not valid")
        payment()





messagefirst()
message()
menu()

messagelast()
