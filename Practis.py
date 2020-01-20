import pygame
import math
import random


class Dog():
    def __init__(self, wight, height, type):
        self.wight = wight
        self.height = height
        self.type = ""
        self.sex = "M"
    def bark(self):
        print("Brak!")
    def stats(self):
        print("Dog wight,", self.wight)
        print("Dog height,", self.height)
        print("Dog is,",type)
    def restatus(self):
        self.wight += 20
        self.height += 20

class Food():
    def __init__(self):
        self.food_x =
        self.food_y =
    def food_creating(self):

dog = Dog(14, 26, "Corgi")
dog.bark()
dog.stats()
dog.restatus()
dog.stats()
