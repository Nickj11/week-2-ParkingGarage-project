#William project
class Parking_deck():
    'Parking deck floors avilable'
    def __init__(self, deck, open, payment):
        self.ticket = deck
        self.open = open
        self.payment = payment
        
    Tickets_Spaces = ["T1", "T2", "T3", "T4", "T5"]
    Account =  []
    while True:


        ticket= input("Welcome, please choose option, tickets/open/quit ")
        
        if ticket == "tickets":
            print(f'You have choosen 1 spot {Tickets_Spaces[0]}')
            #spaces = input("You have choosen 1 space, please press enter ")
            del Tickets_Spaces[0]
        elif ticket =="open":
            print("available spaces are ....")
            print(Tickets_Spaces)
        elif ticket == "quit":
            print("Please provide payment before exit")
            break
        



        
        y = int(input("1 space = $5.00. Please enter 5 for $5.00 payment"))
        
        if y == 5:
            Account.append(y)
            print(f'Thank you for payment, please proceed')
            break
        else: 
            print("ticket is not paid connot proceed")
            continue

        


# I wanted to incorporate an option to view open spots even after paying not sure how to. 
    def availability():
        Tickets_Spaces = ["T1", "T2", "T3", "T4", "T5"]
        availablity = input("Do you wish to view available spots y/n ? ")
        if availablity == "y":
            print(f'Here are available tickets/spaces.... ')
            Tickets_Spaces
        if availablity == "n ":
            print("Thank you, try again")




Spaces = Parking_deck(1, "5.00", 5)
