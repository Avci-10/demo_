# class WeekDayError(Exception):
#         def __init__(self):
#             self.message='this day do not exist'
#             super().__init__()

# class Weeker:
#     week=['mon','tue','wed','thr','fri','sat','sun']
#     def __init__(self, day):
#         if day.lower() in Weeker.week :
#             self.day=day
#         else:
#             raise WeekDayError()


#     def __str__(self):
#       return self.day

#     def add_days(self, n):
#         self.day=Weeker.week[n%7]


#     def subtract_days(self, n):
#          pos=Weeker.week.index(self.day)
#          self.day=Weeker.week[pos-n%7]


# try:
#  weekday = Weeker('Mon')
#  print(weekday)
#  weekday.add_days(15)
#  print(weekday)
#  weekday.subtract_days(23)
#  print(weekday)
#  weekday = Weeker('Monday')
# except WeekDayError as e :
#  print("Sorry, I can't serve your request.")
#  print(e.message)
#  print(type(e))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------


# from math import dist
# class Point:
#     def __init__(self, x=0.0, y=0.0):
#        self.__x=x
#        self.__y=y


#     def getx(self):
#         return self.__x

#     def gety(self):
#        return self.__y

#     def distance_from_xy(self, x, y):
#        return dist((self.getx(),self.gety()),(x,y))

#     def distance_from_point(self, point):
#        assert isinstance(point,Point),'objectError'
#        return dist((self.getx(),self.gety()),(point.getx(),point.gety()))


# point1 = Point(0, 0)
# point2 = Point(1,1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))
# ------------------------------------------------------------------------------------------------------------------------------------


# import math

# class Point:
#     def __init__(self, x, y):

#         self.x = x
#         self.y = y

#     def distance(self, other):

#         return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):

#         self.vertice1 = vertice1
#         self.vertice2 = vertice2
#         self.vertice3 = vertice3

#     def perimeter(self):
#         # Calculate the distances between the vertices
#         side1 = self.vertice1.distance(self.vertice2)
#         side2 = self.vertice2.distance(self.vertice3)
#         side3 = self.vertice3.distance(self.vertice1)

#         # Return the sum of the side lengths
#         return side1 + side2 + side3


# # Example usage
# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(f"The perimeter of the triangle is: {triangle.perimeter()}")
# -------------------------------------------------------------------------------------------------------------
# import time

# class Tracks:
#     def change_direction( self,left, on):
#         print("tracks: ", left, on)


# class Wheels:
#     def change_direction(self, left, on):
#         print("wheels: ", left, on)


# class Vehicle:
#     def __init__(self, controller):
#         self.controller = controller

#     def turn(self, left):
#         self.controller.change_direction(left, True)
#         time.sleep(0.25)
#         self.controller.change_direction(left, False)


# wheeled = Vehicle(Wheels())
# tracked = Vehicle(Tracks())


# wheeled.turn(True)
# tracked.turn(False)
# --------------------------------------------------------------------------
# class Wheels:
#     @classmethod   # METHODE DE CLASSE
#     def description(cls): # CLS KIMA SELF FEL INSTANCE
#         return "I control the wheels of a vehicle."
#     def __init__(self):
#         pass
#     def affichage(self):
#         print('methode dinstance')
# # Appel de la méthode de classe
# print(Wheels.description())  # Fonction de classe appelée directement via la classe
# request=Wheels()
# request.affichage()
#
# ----------------------------------------------------------------------------
# class Dog:
#     kennel = 0

#     def __init__(self, breed):
#         self.breed = breed
#         Dog.kennel += 1

#     def __str__(self):
#         return self.breed + " says: Woof!"


# class SheepDog(Dog):
#     def __str__(self):
#         return super().__str__() + " Don't run away, Little Lamb!"


# class GuardDog(Dog):
#     def __str__(self):
#         return super().__str__() + " Stay where you are, Mister Intruder!"

# class LowlandDog(SheepDog):
#     def __str__(self):
#         return Dog.__str__(self) + " I don't like mountains"

# request = LowlandDog("yessine")
# print(request)

# -------------------------------------------------------------------------------------------------
# how to write a tree function  with python
# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")

#     print(thisclass.__name__)

#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)


# print_exception_tree(SystemExit)
# -------------------------------------------------------------------------------------------
# class PizzaError(Exception):
#     def __init__(self, pizza, message):
#         Exception.__init__(self, message)
#         self.pizza = pizza


# class TooMuchCheeseError(PizzaError):
#     def __init__(self, pizza, cheese, message):
#         PizzaError.__init__(self, pizza, message)
#         self.cheese = cheese


# def make_pizza(pizza, cheese):
#     if pizza not in ['margherita', 'capricciosa', 'calzone']:
#         raise PizzaError(pizza, "no such pizza on the menu")
#     if cheese > 100:
#         raise TooMuchCheeseError(pizza, cheese, "too much cheese")
#     print("Pizza ready!")

# for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
#     try:
#         make_pizza(pz, ch)
#     except TooMuchCheeseError as tmce: # print(tmce )------> affiche le contenu de tmce.args
#         print(tmce, ':', tmce.cheese)
#     except PizzaError as pe:
#         print(pe, ':', pe.pizza)
#-------------------------------------------------------------------------------
# class Fib:
#     def __init__(self, nn):
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1

#     def __iter__(self):
#         print("Fib iter")
#         return self

#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret

# class Class:
#     def __init__(self, ne):
#         self.__n = ne
#         self.__i=0

#     def __iter__(self):
#         print("Class iter")
#         return self
# object = Class(8)

# print(iter(object))
#-----------------------------------------------------------------------------------
# from os import strerror
# from collections import Counter
# # C:/Users/HKIRI JR/Desktop/file.txt
# try:
#     file=input('enter the file name ')
#     with open(file, 'wt') as f:
#         print('exist')
#         f.write('cBabAa'.lower())
        
#     with open(file, 'rt') as f:    
#         src=f.read() 
#         dictt=Counter(src)
#         print(dictt)
        
#     for i,j in dictt.items():
#         print(i,j,sep=' -> ')
# except IOError as e :
#     print(' Cannot create the destination file  ', strerror(e.errno))   #errno taatik num mte3 error w strerror convertit le num en un message 

#------------------------------------------------------------------------------
# C:/Users/HKIRI JR/Desktop/file.txt
class FileError(Exception):
    """Base class for file-related errors."""
    pass

class BadLineError(FileError):
    """Raised when a bad line is detected in the file."""
    def __init__(self, line,parts):
         super().__init__(f"Bad line detected: {line} : {parts} should be a number")
         self.line = line
         self.parts=parts
        
        
class EmptyFileError(FileError):
    """Raised when the source file exists but is empty."""
    def __init__(self, filename):
        super().__init__(f"The file '{filename}' is empty.")
        self.filename = filename
        

def read_file_and_generate_report(filename):
    try:
        # Open the file and read the lines
        with open(filename, 'rt') as f:
            lines = f.readlines()
            

        # Check if the file is empty
        if not lines:
            raise EmptyFileError(filename)

        # Dictionary to store student data
        student_points = {}

        # Process each line
        for line in lines:
            line = line.strip()
            if not line:
                continue  # Ignore empty lines
            parts = line.split()  # Split by whitespace
            if len(parts) != 3:
                raise BadLineError(line,parts)  # Bad line structure
            first_name, last_name, points = parts
            try:
                points = float(points)  # Convert points to float
            except ValueError:
                raise BadLineError(line,points)  # Points are not a valid number

            # Create full name and update points
            full_name = f"{first_name} {last_name}"
            if full_name in student_points:
                student_points[full_name] += points
            else:
                student_points[full_name] = points
        # Generate the sorted report
        print("\nSorted Report:",'\n')
        for name, total_points in sorted(student_points.items()):
            print(f"{name} \t {total_points:.1f}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except EmptyFileError as e:
        print(e)
    except BadLineError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Main program
if __name__ == "__main__":
    # from datetime import datetime
    # with open('logs','wt') as file :
    #     file.write('HI CODERS'+'\n')
    #     file.write(str(datetime.now().time()))
    # with open('logs','rt') as f:
    #     x=f.read()
    #     print(x)

    filename = input("Enter the file name: ")
    read_file_and_generate_report(filename)




     

