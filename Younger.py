print("-"*90)
class People:

	def __init__(self,people):
		self.people = people

	def get_people(self):
		print("Given persons are {}".format(self.people))
		print()

	def get_names(self):
		print(self.people.keys())

	def get_younger1(self):
		min_name = None
		min_age = None
		for name in self.people.keys():
			age = self.people[name]
			if min_age is None:
				min_name = name
				min_age = age
			elif age < min_age:
				min_name = name
				min_age = age
		return min_name

	def get_age(self,name):
	 	print(self.people.get(name))

	def get_min(self):
		return min(self.people,key=self.people.get)



p = People({"chandu":19 , "lucky":22 ,"randy":16})

p.get_people()
g=p.get_min()

print()
#print(min(p.people.keys()))
print("Younger Among Them is : '{}' ".format(g))
print("-"*90)

