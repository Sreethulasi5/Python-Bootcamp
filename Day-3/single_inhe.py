class vehicle():
    def break_fun():
        print("adjust the sudden speed")
    def clutch():
        print("it will stop the vehicle")
    def accelerator():
        print(" it willraise the speed")
class car(vehicle):
    def horn():
        print("it will make horn when somebody comes over")
    def wheels():
        print("it will have 4 wheels")
    def steering():
        print("it will handle the direction" )
veh=car
car.break_fun()
car.accelerator()
car.horn()
