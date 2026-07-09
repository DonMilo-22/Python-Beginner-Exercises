Name = ""
Grade1 = int()
Grade2 = int()
Grade3= int()

Name = input("Student Name: ")
Grade1 = int(input("Grade 1: "))
Grade2 = int(input("Grade 2: "))
Grade3 = int(input("Grade 3: "))

average = (Grade1 + Grade2 + Grade3)/3

print("Average: ",average)
if average >= 70:
    print("Status: Passed")
else:
    print("Status: Failed")