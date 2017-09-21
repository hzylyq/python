#create a mapping of state to abbreviation
states = {
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}

#create a basic set of state and some cities in them
cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

#and some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is", states['Florida'])
print('-' * 10)

#do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
print('-' * 10)

#print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():######将states中的两个值分别赋给state和abbrev
	print("%s has the city %s" % (state, abbrev))
print('-' * 10)

#now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
	print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-' * 10)
#safely get a abbreviation by state that might not be there
state = states.get('Texas', None)		#return False

if not state:
	print("Sorry, no Texas")

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)