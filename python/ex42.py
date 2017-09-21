# -*- coding: utf-8 -*-

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog
class Dog(Animal):
	def __init__(self, name):
		##Dog's name
		self.name = name

##Cat
class Cat(Animal):
	def __init__(self, name):
		##Cat's name
		self.name = name


##Person not animal
class Person(object):
	def __init__(self, name):
		##Person's name
		self.name = name
		##Person has-a pet of some kind
		self.pet = None

class Employee(Person):
	def __init__(self, name, salary):
		##?? hmm what is this strange magic?
		##将父类也就是Person的name方法应用到子类Employee上
		super(Employee, self).__init__(name)
		##Employee has salary
		self.salary = salary
##定义了fish类
class Fish(object):
	pass

##定义了salmon类，salmon继承于fish类
class Salmon(Fish):
	pass

##定义Halibut类，Hali继承于fish类
class Halibut(Fish):
	pass

##rover是从dog类中抽象出来的一个对象，rover的name是“Rover”
rover = Dog("Rover")

##satan是从Cat类中抽象出来的一个对象，satan的name是“Satan”
satan = Cat("Satan")

##mary是Person的一个对象，mary的name是“Mary”
mary = Person("Mary")
mary.pet = satan

##frank 是employee,他的salary是12000
frank = Employee("frank", 12000)
frank.pet = rover

##filpper is a fish
filpper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()





		
