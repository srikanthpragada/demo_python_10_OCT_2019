marks_list = {}

while True:
    rollno = int(input("Enter rollno [0 to stop] :"))
    if rollno == 0:
        break

    marks = int(input("Enter marks :"))
    if rollno not in marks_list:
        marks_list[rollno] = [marks]   # add rollno and list for marks
    else:
        marks_list[rollno].append(marks)  # append marks to existing list


for rollno,marks in sorted(marks_list.items()):
    print(rollno, marks, sum(marks))
