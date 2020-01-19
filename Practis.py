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
        print("Dog wight,", wight)
        print("Dog height,", height)
        print("Dog is,",type)
    def restatus(self):
        wight += 20
        height += 20
dog = Dog(14, 26, "Corgi")
dog.bark()
dog.stats()
dog.restatus()
dog.stats()
