class Car:
    __drive = False
    __direction = ''
    def __init__(self,speed,color,name,is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police:
            print("Это полицейская машина. Этой машине можно все ))))) ")
        self.go(self.speed)


    def go(self,speed):
            print(f'Машина поехала со скоростью {speed}')

    def stop(self):
        print(f'Машина остановилась')
        self.speed = 0

    def turn(self,direction):
        self.__direction = direction
        print('Вы совершили ', self.__direction)

    def show_speed(self):
        return self.speed

    def set_speed(self,new_speed):
        self.speed = new_speed

class TownCar(Car):
    def __init__(self,speed,color,name,is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.go(self.speed)

        if self.show_speed() > 60:
            print("Необходимо снизить скорость")


    def check_speed(self):
        if self.speed > 60:
            print("Присутствует наушение скорости")
        return self.speed

class SportCar(Car):
    pass

class WorkCar(Car):
    def __init__(self,speed,color,name,is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        if self.show_speed() > 40:
            print("Необходимо снизить скорость")

        self.go(self.speed)

    def check_speed(self):
        if self.speed > 40:
            print("Присутствует наушение скорости")
        return self.speed

class PoliceCar(Car):
    pass



print("Town Car")
tow_car = TownCar(70,'Red',"Mazda")
tow_car.set_speed(50)
print(tow_car.check_speed())
tow_car.go(50)


print("Sport Car")
sport_car = SportCar(170,'Blue',"Ferarry")
sport_car.set_speed(220)
print(sport_car.show_speed())

print("Work Car")
tow_car = TownCar(70,'Gree',"Niva")
tow_car.set_speed(40)
print(tow_car.check_speed())

print("Police CAR")
police_car = PoliceCar(330,"White","SuperPuper",True)
police_car.turn("Left")
police_car.turn("Right")
police_car.turn("Reversal он же разворот")
print(police_car.show_speed())
police_car.go(50)
police_car.stop()
police_car.go(144)
