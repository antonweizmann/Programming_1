
print("What year is it?")
while True:
	try:
		cur_year = int(input())
		break;
	except ValueError:
		print("Invalid Input! Please enter a valid number")
print("What is your birth year?")
while True:
	try:
		birth_year = int(input())
		break;
	except ValueError:
		print("Invalid Input! Please enter a valid number")

print("Age is " + str(cur_year - birth_year))
