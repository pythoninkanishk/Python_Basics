# 6. Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects. 


import random
class Train():
    def __init__(slf, TrainNo):
        slf.TrainNo = TrainNo

    def BookTicket(slf, fro, to):
        print(f"Your Train No {slf.TrainNo} has been booked From {fro} to {to}")

    def Getstatus(slf):
        print(f"Your Train No {slf.TrainNo} is coming right on time")

    def getFair(Slf, fro, to ):
        print(f"Your Fair for the train no {Slf.TrainNo} from {fro} to {to} is {random.randint(200, 1000)}")
A = Train(1409)
A.BookTicket("Rampura", "Jaipur")
A.Getstatus()
A.getFair("Rampura", "Jaipur")


#YES YOU CAN CHANGE "self - Parameter" TO "slf"
# NOW LETS TRY "HARRY"

import random
class Plane():
    def __init__(Harry, FlightNo):
        Harry.FlightNo = FlightNo

    def BookTicket(Harry, fro, to):
        print(f"Your Flight No {Harry.FlightNo} has been booked From {fro} to {to}")

    def Getstatus(Harry):
        print(f"Your Flight No {Harry.FlightNo} is coming right on time")

    def getFair(Slf, fro, to ):
        print(f"Your Fair for the Flight no {Slf.FlightNo} from {fro} to {to} is {random.randint( 1000, 10000)}")
B = Plane(1409)
B.BookTicket("NYK", "BLR")
B.Getstatus()
B.getFair("NYK", "BLR")

# Hence, "Harry" Can also be used as self parameter