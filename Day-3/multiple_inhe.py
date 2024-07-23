class vehicle():
    def break_fun():
        print("adjust the sudden speed")
    def clutch():
        print("it will stop the vehicle")
    def accelerator():
        print(" it willraise the speed")
class dcm():
    def horn_dcm():
        print("it will make horn when somebody comes over")
    def wheels():
        print("it will have 10 wheels")
    def steerings():
        print("it will handle the direction" )
class car(vehicle,dcm):
    def horn():
        print("it will make horn when somebody comes over")
    def wheels():
        print("it will have 4 wheels")
    def steering():
        print("it will handle the direction" )
cobj=car
cobj.horn()
cobj.wheels()
cobj.clutch()
cobj.steerings()