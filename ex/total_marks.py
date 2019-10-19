
marks_list = {}

while True:
    rollno = int(input("Enter rollno [0 to stop] :"))
    if rollno == 0:
        break

    marks = int(input("Enter marks :"))
    if rollno not in marks_list:
        marks_list[rollno] = marks   # add new entry
    else:
        marks_list[rollno] += marks  # add marks to existing total


for rollno,total in sorted(marks_list.items()):
    print(rollno, total)
