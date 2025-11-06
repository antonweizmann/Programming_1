days = ["Mon" ,"Tue" , "Wed" , "Thu" , "Fri" ]

tasks = {}
for i in range(5):
    tasks[days[i]] = []
    for x in range(int(input("How many tasks do you have for " + days[i] + "\n"))):
        tasks[days[i]].append(input("Task number " + str(x) + "\n"))

print("Which day is today? ", end="")
print(days)
cur_day = input()
print("Here is your list of tasks for today:")
for x in tasks[cur_day]:
    print(x)