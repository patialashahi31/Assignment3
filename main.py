child = []
adult = []
senior = []
totalCost=[]
concession = []
child.append(0)
adult.append(0)
senior.append(0)
totalCost.append(0)
concession.append(0)

from ticket import Ticket
from checkout import Checkout

h = Ticket()
h.setSeniorTicketPrice(15)
h.setChildTicketPrice(10)
h.setAdultTicketPrice(20)
h.setConcessionTicketPrice(17)

def messagefirst():
    for j in range(0,50):
        print("*",end="")



def message():
    print()
    print()
    print("Ticket Sales")
    print("Program Developer == xyz")
    print("Student ID = 123 ")
    print("Federation University Australia Robot wars Tickets")
    print()


def menu():
    number_of_senior_tickets = 0
    number_of_adult_tickets = 0
    number_of_child_tickets =0
    number_of_concession_tickets = 0
    print("Type of Tickets")
    print()
    print("1. Child")
    print("2. Adult")
    print("3. Senior citizen")
    print("4. Concession")
    n = int(input())
    a = [1,2,3,4]
    while(n in a):
        if(n==1):
            print("Number of Child tickets")
            number_of_child_tickets = int(input())
            child[0] = number_of_child_tickets
            print("Do you want to add more tickets?(Y/N)")
            choice = input()
            if(choice.lower()=='y'):
                menu()
                break
            else:
                bill()
                break
        elif (n==2):
            print("Number of Adult tickets")
            number_of_adult_tickets = int(input())
            adult[0] = number_of_adult_tickets
            print("Do you want to add more tickets?(Y/N)")
            choice = input()
            if (choice.lower() == 'y'):
                menu()
                break
            else:
                bill()
                break
        elif(n==3):
            print("Number of Senior Citizen tickets")
            number_of_senior_tickets = int(input())
            senior[0] = number_of_senior_tickets
            print("Do you want to add more tickets?(Y/N)")
            choice = input()
            if (choice.lower() == 'y'):
                menu()
                break
            else:
                bill()
                break
        elif(n==4):
            print("Number of Concession tickets")
            number_of_concession_tickets = int(input())
            concession[0] = number_of_concession_tickets
            print("Do you want to add more tickets?(Y/N)")
            choice = input()
            if (choice.lower() == 'y'):
                menu()
                break
            else:
                bill()
                break
        else:
            print("Please enter valid number")
            menu()
            break



def bill():
    print("You bought")
    print("Price of "  + str(child[0]) + " child tickets " + " : " + str(h.getChildTicketPrice()) +
          " * " + str(child[0]) + " = " + str(h.getChildTicketPrice()*child[0]) + " dollars")
    print("Price of " + str(adult[0]) + " Adult tickets " + " : " + str(h.getAdultTicketPrice()) +
          " * " + str(adult[0]) + " = " + str(h.getAdultTicketPrice() * adult[0]) + " dollars")
    print("Price of " + str(senior[0]) + " senior tickets " + " : " + str(h.getSeniorTicketPrice()) +
          " * " + str(senior[0]) + " = " + str(h.getSeniorTicketPrice() * senior[0]) + " dollars")
    print("Price of " + str(concession[0]) + " concession tickets " + " : " + str(h.getConcessionTicketPrice()) +
          " * " + str(concession[0]) + " = " + str(h.getConcessionTicketPrice() * concession[0]) + " dollars")
    print("")
    total = child[0]*h.getChildTicketPrice() + adult[0]*h.getAdultTicketPrice()+senior[0]*h.getAdultTicketPrice()+concession[0]*h.getConcessionTicketPrice()
    totalCost[0] = total

    print("Total : " + str(total) + " dollars" )
    print()
    print("1. Checkout")
    print("2. More tickets")

    n = int(input())
    a = [1,2]
    while(n in a):
        if (n==1):
            payment()
            break;
        elif(n==2):
            menu()
            break
        else:
            print("Please enter valid number")
            n = int(input())


check = Checkout()


def payment():
    transactionId=0;
    print("Enter credit card details: ")
    print("Enter name(As on credit card) : " )
    name = input()
    check.setName(name)
    print("Enter credit card number")
    card_number = int(input())
    if(check.isValid(card_number)):
        print("Enter expiry month")
        month = int(input())
        print("Enter expiry year")
        year = int(input())
        if(check.expiryDate(month,year)):
            print("Enter cvv number")
            cvv_number = int(input())
            if(check.cvv(cvv_number)):
                check.setName(name)
                check.setCreditCardNumber(card_number)
                h.setTotal(totalCost[0])
                print("Payment successful")
                transactionId = transactionId + 1
                print("Your unique transaction Id number :" + str(transactionId))
                file1 = open("transactions.txt","w")
                l = ["Transaction ID : " +str(transactionId) + " "+"\nName : " +
                     check.getName() + "\nNumber of child Tickets: " + str(child[0])
                     +" \nNumber of Adult tickets : " + str(adult[0])+
                     " \nNumber of Senior Citizen tickets: "+ str(senior[0])
                     +" \nNumber of concession tickets: "
                     +" \nTotal Cost = " + str(totalCost[0]) + " dollars"]
                file1.writelines(l)
                file1.close()
            else:
                print("Wrong cvv number")
                payment()
        else:
            print("Card is expiry of date is invalid")
            payment()
    else:
        print("Card number is not valid or Card is expired")
        payment()





messagefirst()
message()
messagefirst()
print()
menu()


