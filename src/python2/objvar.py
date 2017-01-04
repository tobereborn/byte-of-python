#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

class Person:
    ''' Represents a person.'''
    population = 0
    
    def __init__(self, name):
        '''Initializes the person.'''
        self.name = name
        print'(Initializing %s)' % self.name
        Person.population += 1
        
    def sayHi(self):
        '''Greets the other person.'''
        print 'Hi,my name is %s' % self.name
    
    def howMany(self):
        '''Print the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %s persons here.' % \
            Person.population

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany
