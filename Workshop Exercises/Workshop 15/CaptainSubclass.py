#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:22:26 2021

@author: Matthew
"""

class Person:
    def __init__(self, first_name, surname, birth_year, occupation):
        self.first_name = first_name
        self.surname = surname
        self.birth_year = birth_year
        self.occupation = occupation
    def age(self, year):
        timegap = year - self.birth_year
        if timegap > 0:
            age = timegap
        elif timegap == 0:
            age = f'{self.first_name} {self.surname} will be born this year'
        else:
            timegap = abs(timegap)
            age = f'{self.first_name} {self.surname} will be born in {timegap} years'
        print(age)
    def __str__(self):
        return(f'{self.first_name} {self.surname} {self.occupation}')
    def same_occupation_age(self, Person2): #We pass 2 objects to this function, self and person2
        if self.occupation == Person2.occupation:
            print(f'{self.first_name} and {Person2.first_name} have the same occupation')
        if self.birth_year == Person2.birth_year:
            print(f'{self.first_name} and {Person2.first_name} have the same age')
        
    

class Captain(Person):
    def __init__(self, first_name, surname, birth_year, ship, loyalty):
        super().__init__(first_name, surname, birth_year, 'Ship Captain') #Ensures occupation is always ship captain
        self.ship = ship
        self.loyalty = loyalty
        print(f'Captain {self.first_name} {self.surname} reporting for duty!')
    def swashbuckle(self):
        print(f'For king and the {self.loyalty}')



Pirate = Captain('Horatio', 'Nelson', 1758, 'HMS Victory', 'United Kingdom')
Pirate.age(1658)
print(Pirate)