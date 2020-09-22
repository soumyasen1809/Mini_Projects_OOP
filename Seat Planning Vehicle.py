# http://cppprojectcode.blogspot.com/2010/09/seat-planning-of-vehicle.html
# Seat Planning of vehicle - easily plan the seats of a vehicle

import random


class Seat:

    def __init__(self, seatnumber, seattype, reservestatus):
        self.seatnumber = seatnumber
        self.seattype = seattype
        self.reservestatus = reservestatus                  # Reserve status = 0 for unreserved and 1 for reserved seat


class Customer:

    def __init__(self, name, destination, ticketcost):
        self.name = name
        self.destination = destination
        self.ticketcost = ticketcost
        self.ticketnumber = random.randint(1000,2000)       # Ticked ID is a randomly generated number
        self.seatreserved = []                              # List is chosen, incase multiple seats per customer allowed


class SeatManagement:

    def __init__(self, seat, customer):
        self.seat = seat
        self.customer = customer

    def assignSeat(self):
        if self.customer.seatreserved == []:                # 1 seat per customer only
            self.seat.reservestatus = 1                     # Change seat status to reserved when booked
            self.customer.seatreserved.append(self.seat)    # Assign the seat details to the customer
        else:
            print ("Seat already taken! Choose a different one")

    def removeSeat(self):
        if self.customer.seatreserved == []:
            print ("Seat is not filled yet!")
        else:
            self.seat.reservestatus = 0
            self.customer.seatreserved.remove(self.seat)    # Remove the seat details from the customer


class DisplayData:

    def __init__(self, customerlist, seatlist):
        self.customerlist = customerlist
        self.seatlist = seatlist

    def customerDetails(self, customer):
        self.customer = customer
        print ("------------------ Customer Details ------------------")
        print ("Customer Name: \t" + str(self.customer.name))
        print ("Destination: \t" + str(self.customer.destination))
        print ("Ticket Cost: \t" + str(self.customer.ticketcost))
        print ("Ticket Number: \t" + str(self.customer.ticketnumber))
        print ("Seat Number: \t" + str(self.customer.seatreserved[0].seatnumber))
        print ("------------------ ---------------- ------------------")

    def seatDetails(self, seat):
        self.seat = seat
        print ("------------------ Seat Details ------------------")
        print ("Seat Number: \t" + str(self.seat.seatnumber))
        print ("Seat Type: \t" + str(self.seat.seattype))
        if self.seat.reservestatus == 0:
            print ("Status: \t" + "Unreserved")
        elif self.seat.reservestatus == 1:
            print ("Status: \t" + "Reserved")
        # print ("Status: \t" + str(self.seat.reservestatus))
        print ("------------------ ------------ ------------------")

    def searchCustomerName(self, inputname):
        self.inputname = inputname
        count = 0

        for i in range(len(customerlist)):
            if self.inputname == customerlist[i].name:
                DisplayData(customerlist, seatlist).customerDetails(customerlist[i])
                count = count + 1
        if count == 0:
            print ("Customer " + str(self.inputname) + " not found!")

    def searchSeatNumber(self, inputnumber):
        self.inputnumber = inputnumber
        count = 0

        for i in range(len(seatlist)):
            if inputnumber == seatlist[i].seatnumber:
                DisplayData(customerlist, seatlist).seatDetails(seatlist[i])
                count = count + 1
        if count == 0:
            print ("Seat number " + str(self.inputnumber) + " doesn't exist!")


# Enter data
s1 = Seat(12, "Standard", 0)        # Enter status = 0 for unreserved seat
s2 = Seat(9, "Premium", 0)
s3 = Seat(46, "Premium", 0)

c1 = Customer("Hank", "NYC", 12.98)
c2 = Customer("Tom", "Calgary", 90.21)

customerlist = [c1, c2]
seatlist = [s1, s2, s3]

# Operations
SeatManagement(s1, c1).assignSeat()
SeatManagement(s2, c2).assignSeat()
SeatManagement(s1, c1).removeSeat()
SeatManagement(s3, c1).assignSeat()
SeatManagement(s2, c2).removeSeat()
SeatManagement(s1, c2).assignSeat()

# Print all customer details
print ("\n All Customer details below \n")
DisplayData(customerlist, seatlist).customerDetails(c1)
DisplayData(customerlist, seatlist).customerDetails(c2)

# Print all seat details
print ("\n All Seat details below \n")
DisplayData(customerlist, seatlist).seatDetails(s1)
DisplayData(customerlist, seatlist).seatDetails(s2)
DisplayData(customerlist, seatlist).seatDetails(s3)

# Print based on customer name search and seat number search
print ("\n Search - customer name and seat number \n")
DisplayData(customerlist, seatlist).searchCustomerName("Tom")
DisplayData(customerlist, seatlist).searchCustomerName("Tony")
DisplayData(customerlist, seatlist).searchSeatNumber(12)
DisplayData(customerlist, seatlist).searchSeatNumber(28)
