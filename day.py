print("-"*90)
print()
days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def findDay(day,no_days):

	result = ""

	for index, match in enumerate(days):

		if match==day:
			index +=no_days

			if index >= len(days):
				index = index % len(days)
				result = days[index]
				
			else:

				result = days[index]

		
	return "Given day is '{}' after '{}' day/ day's the day we get '{}'.".format(day,no_days,result)


print(findDay("saturday",5))           #Enter given day and no of days here.....

print()
print("-"*90)



    
