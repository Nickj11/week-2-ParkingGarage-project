
Pspaces = [ "P1" , "P2" , "P3" , "P4"]
class Parkinglot():
    def __init__(self):
        self.ticket = 4
    Pspaces = [ "P1" , "P2" , "P3" , "P4"]
    while True:

            Lot = input("what would you like to do?: Park\Ticket\leave\Open:  ")
            if Lot.lower() == "park":
                print(f'Park your car {Pspaces[0]}')
                Pspaces.remove("P1")
                break
            elif Lot.lower() == "leave":
                print(f'You must make a payment 5 dollors')
            elif Lot.lower() == "ticket":
                print(f'here is your ticket')
            elif Lot.lower() == "open":
                print(f'here are your spot:{Pspaces}')
                
            else:
                print("invailed options, options are Park\Ticket\leave\Open")
            

            
            

class Pay(Parkinglot):
    def __init__(self):
        while True:
            payment = int(input("thank you for coming you total amount is 5 dollars:  "))
            if payment == 5:
                    print("thank you for the amount you have 15 minutes to leave")
                    break

            elif payment < 5:
                print("please pay the amount that is owe 5 dollars")

            elif payment > 5:
                print("Declined amount to much")
            else:
                print('invailed options')
class LeaveGarage(Parkinglot):
    def __init__(self):
            payment = 5
            if payment == 5:
                Pspaces.append("P1")
                print("Thank you come again")
            else:
                 print("Did you forget to pay? ")
        

car_1 = Parkinglot()
Car_1 = Pay()
car_1= LeaveGarage()
