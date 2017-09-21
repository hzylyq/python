# -*- coding: utf-8 -*-
class Parent(object):
	def altered(self):
		print "Parent altered"
	
class Child(Parent):
	def altered(self):
		print "CHILD BEFORE PARENT altered"
		super(Child, self).altered()
		print "CHILD AFTER PARENT altered"		
		
dad = Parent()
sun = Child()

dad.altered()
sun.altered()
		