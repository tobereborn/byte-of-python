#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchooolMember: %s)' % self.name
    
    def tell(self):
        print 'Name: "%s" Age: "%s"' % (self.name, self.age)
           
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name
    
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d"' % self.salary
    
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name
    
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "%d"' % self.marks
    
t = Teacher('Mrs.Abraham', 40, 30000)
s = Student('Swaroop', 21, 75)

print

members = [t, s]
for member in members:
    member.tell()