def Ping_Status(Ping):
   
    match Ping:
        case _ if 200 <= Ping < 1000:
            return "Ping too High :/"
        case _ if 100 <= Ping < 200:
            return "High Ping"
        case _ if 50 <= Ping < 100:
            return "Normal Ping"
        case _ if 1 <= Ping < 50:
            return "Fast Ping"
        case _:
            return "Invalid Ping"
print(Ping_Status(150))