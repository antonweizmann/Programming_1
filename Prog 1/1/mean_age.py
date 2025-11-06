import statistics

input_num = ["first", "second", "third"]
print("What year is it?")
while True:
	try:
		cur_year = int(input())
		break;
	except ValueError:
		print("Invalid Input! Please enter a valid number")


print("What is the first birth year?")
while True:
	try:
		birth_year1 = int(input())
		age1 = cur_year - birth_year1
		break;
	except ValueError:
		print("Invalid Input! Please enter a valid number")

print("What is the first birth year?")
while True:
	try:
		birth_year2 = int(input())
		age2 = cur_year - birth_year2
		break;
	except ValueError:
		print("Invalid Input! Please enter a valid number")
print("What is the first birth year?")
while True:
	try:
		birth_year3 = int(input())
		age3 = cur_year - birth_year3
		break;
	except ValueError:
		print("Invalid Input! Please enter a valid number")

print("The input years were: " + str(birth_year1) + ", " + str(birth_year2) + " and " + str(birth_year3))

print("The probable ages are: " + str(age1) + ", " + str(age2) + " and " + str(age3))

print("The average age is " + str(statistics.mean([age1, age2, age3])))
