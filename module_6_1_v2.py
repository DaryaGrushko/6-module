#Зачем нужно наследование
#Задача "Съедобное, несъедобное"

class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.adiable==True:
            print (self.name, 'съел', food.name)
            self.fed = True
        else:
            print (self.name, 'не стал есть', food.name)
            self.alive = False

class Plant:
    adiable = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    adiable = True
    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
print ('----------')
a1.eat(p1)
print ('----------')
a2.eat(p2)
print ('----------')
print(a1.alive)
print(a2.fed)
