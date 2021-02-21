import getpass
import itertools

print("Create Account")
userName = input("Username: ")
password = getpass.getpass("Password: ")
name = input("Name: ")
print("\nWelcome " + name)

print("Select Intensity Level")
print("   1. Beginner")
print("   2. Intermediate")
print("   3. Advanced")
level = int(input("Level: "))



print("\nWhat equipment do you have available(can select multiple)?")
equipmentArr = ["Treadmill", "Resistence Bands", "Resistence Band Loops", "Yoga Mat",
                "Dumbells", "Bench Press", "Pull Up Bar", "Kettle Bell", "Jump Rope", "NONE"]
for i in range(len(equipmentArr)):
    print("   " + str(i+1) + ". " + equipmentArr[i])
equipment = input("Equipment: ")

equipList = equipment.split(",")
for i in range(len(equipList)):
    equipList[i] = int(equipList[i])

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
timeArr = ["0-10", "10-15", "15-20", "20-30", "30+"]
areaArr = ["Chest", "Back", "Arms", "Abs", "Legs", "Shoulders", "Cardio", "Calves", "Glutes",
           "Forearms", "Quads", "Triceps"]
daysArr = [None]*5

for j in range(len(days)):
    print("\n"+days[j] + " SCHEDULE")
    print("How much time do you have available to workout(can select multiple)?")
    for i in range(len(timeArr)):
        print("   " + str(i+1) + ". " + timeArr[i] + " minutes")
    time = input("Time: ")

    print("\nWhat area would you like to workout on(can select multiple)?")
    for i in range(len(areaArr)):
        print("   " + str(i+1) + ". " + areaArr[i])
    area = input("Areas: ")

    timeList = time.split(",")
    areaList = area.split(",")

    for i in range(len(timeList)):
        timeList[i] = int(timeList[i])
    for i in range(len(areaList)):
        areaList[i] = int(areaList[i])

    a = [[level], equipList, timeList, areaList]
    b = list(itertools.product(*a))
    for i in range(len(b)):
        b[i] = b[i][3] + (10*b[i][2]) + \
            (10**2 * b[i][1]) + (10**3 * b[i][0])

    daysArr[j] = b

print("\n")
for i in range(len(daysArr)):
    print(days[i] + ": " + str(daysArr[i]))
