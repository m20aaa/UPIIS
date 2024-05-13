with open("test_group.csv", "r") as f:
	f.readline()
	data = f.read()

students = {}

for line in data.split("\n"):
	if len(line):
		_ = line.split(";")
		_id = _[0]
		name = _[1]
		dob = _[2]
		if _[3] != "": st_id = _[3]
		subj = _[4]
		doe = _[5]
		mark = int(_[6])
		t_name = _[7]

		if st_id != "" and st_id not in students:
			students.update({f"{st_id}":[name, dob, 0, 0, 0, {}]})
		students[st_id][5].update({subj:mark})
		students[st_id][2]+=mark
		students[st_id][3]+=1
		students[st_id][4]=students[st_id][2]/students[st_id][3]

min_id = list(students)[0]
min_avg = students[min_id][4]

for st_id in students:
	if students[st_id][4] < min_avg:
		min_id = st_id
		min_avg = students[st_id][4]

print("ФИО студента с самой худшей успеваемостью: ", students[min_id][0])
print("Средний балл студента по всем дисциплинам: ", min_avg, "\n")
print("Список дисциплин и оценки:")
a = students[min_id][5]
for i in a:
	print(i, a[i])