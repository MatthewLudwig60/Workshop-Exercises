#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:27:09 2021

@author: Matthew
"""
import random
    
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

class Ship: #QM = Quartermaster, FM = First mate, PM = Powder monkey
    def __init__(self, Captain, QM, FM, PM):
        self.Captain = Captain
        self.QM = QM
        self.FM = FM
        self.PM = PM
        self.swabbies = []
        self.name = Captain.ship
        self.powder_reserve = random.randint(1, 10)
        self.rum_reserve = random.randint(1, 30)
        self.crew = [self.Captain, self.QM, self.FM, self.PM, self.swabbies]
    def load_cannons(self):
        if self.powder_reserve > 0:
            self.powder_reserve += -1
            print(f'{self.PM} fetched the powder, the powder reserve is now {self.powder_reserve}')
        else:
            print('We have no powder left')
    def splice_the_mainbrace(self):
        num_people = len(self.crew)
        if num_people <= self.rum_reserve:
            self.rum_reserve += -(num_people)
            print(f'We have {self.rum_reserve} rations of rum left')
        else:
            print('We do not have enough rum to give everyone a ratio, there is a mutiny!')
    def Shanghai(self, Swabbie):
        self.swabbies.append(Swabbie)
            

Person1 = Person('Jeremy', 'Irons', 1948, 'Actor')
Person2 = Person('Judi', 'Dench', 1934, 'Actor')
Person3 = Person('Ozzy', 'Osbourne', 1948, 'Singer')
Pirate = Captain('Horatio', 'Nelson', 1758, 'HMS Victory', 'United Kingdom')
Ship1 = Ship(Pirate, Person2, Person1, Person3)
# print(Ship1.powder_reserve)
# Ship1.load_cannons()
Person4 = Person('Matt', 'Ludwig', 2002, 'Scientist')
Ship1.Shanghai(Person4)
print(Ship1.rum_reserve)
Ship1.splice_the_mainbrace()

        
    