print()
print("-"*20,"WELCOME TO FLAMES GAME ","-"*20)
print()


person1 = input("Please Enter First Person Name : ") 
print()
person2 = input("Please Enter Second Person Name :")

person1 = person1.replace(' ', '')
person2 = person2.replace(' ', '')
person1a = list(person1)
person1b = list(person1)
person2 = list(person2)

print()


for ch in person1a:
	present = ch in person2
		
	if present:
		person2.remove(ch)
		person1b.remove(ch)

count = len(person1b) + len(person2)

flames = list("flames")

while len(flames)!=1:
	if count > len(flames):
		x = count % len(flames)
	else:
		x= count
	if x == 0:
		flames = flames[:-1]
	else:
		x = x-1
		flames= flames[x+1:] +flames[:x]

print("-"*90)
print()
print()
	

if flames[0]=="f":
	print(" 'FRIENDS' ")

elif flames[0]=="l":
	print(" 'LOVERS' ")

elif flames[0]=="a":
	print(" AFFECTIONATE' ")

elif flames[0]=="m":
	print(" 'MARRIAGE' ")

elif flames[0]=="e":
	print(" 'ENEMIES' ")

elif flames[0]=="s":
	print(" 'SIBLINGS' ")

print()
print()
print("-"*90)








