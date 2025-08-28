# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

import random
class Train():
    def __init__(self, TrainNo):
        self.TrainNo = TrainNo

    def BookTicket(self, fro, to):
        print(f"Your Train No {self.TrainNo} has been booked From {fro} to {to}")

    def Getstatus(Self):
        print(f"Your Train No {Self.TrainNo} is coming right on time")

    def getFair(Self, fro, to ):
        print(f"Your Fair for the train no {Self.TrainNo} from {fro} to {to} is {random.randint(200, 1000)}")
A = Train(1409)
A.BookTicket("Rampura", "Jaipur")
A.Getstatus()
A.getFair("Rampura", "Jaipur")
