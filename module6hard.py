# #Дополнительное практическое задание по модулю "Наследование классов"

import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides):

        self.set_color(*color)
        self.filled = False
        new_side = []

        if self.__is_valid_sides(*sides) :
            self.__sides = list(sides)
        else:
            for i in range(self.sides_count):
                new_side.append(1)
                self.__sides = list(new_side)
                print ('__sides= ', self.__sides)

    def get_color(self):
        #print('def get_color')
        return self.__color

    def __is_valid_color(self, r, g, b):
        #print ('__is_valid_color')
        if 0<= r <= 255 and 0<= g <= 255 and 0<= b <= 255 and isinstance(r, int) and  isinstance(g, int) and  isinstance(b, int):
            #print (' color значения корректные')
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return False

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if not isinstance(side, int):
                    return False
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
class  Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        #print('я в __init__  Circle')
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    def get_square(self):

        sides = self.get_sides()
        p = (sides[0] + sides[1] + sides[2]) / 2
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10, 5) # (Цвет, стороны)
circle2 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
print(circle2.get_color())
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


