#Множественное наследование
#Задача "Ошибка эволюции"
import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init(self, speed, _cords = [0, 0, 0]):
        self._cords = _cords
        swlf.speed = speed
        super().__init__(speed)



    def move(self, dx, dy, dz):
        #print ('self.speed',  self.speed, 'x=', dx, 'y=', dy, 'z=', dz)
        if dz*self.speed<0:
            print ("It's too deep, i can't dive :(")
        else:
            self._cords=[dx*self.speed, dy*self.speed, dz*self.speed]
        #print (dx*self.speed, dy*self.speed, dz*self.speed)
        #print ('self._cords=', self._cords)
    def get_cords(self):
        print ('X:', self._cords[0], ' Y:',  self._cords[1],' Z:', self._cords[2])

    def attack(self):
        print ('self._DEGREE_OF_DANGER = ', self._DEGREE_OF_DANGER)
        if self._DEGREE_OF_DANGER<5:
            print ("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print ('sound = ', self.sound)

class Bird(Animal):
    beak=True
    def __init__(self, speed):
        pass

    def lay_eggs(self):
        print ('Here are(is)', random.randint(1,4) ,'eggs for you')

class AquaticAnimal:
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2]=int(self._cords[2] - abs(dz) / 2 * self.speed)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill( Bird, PoisonousAnimal, AquaticAnimal):

    def __init__(self,  speed, sound = "Click-click-click"):
        self.speed = speed
        self.sound = sound
        super().__init__(speed)

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
