
students = ("Alice", 78), ("Bob", 45), ("Charlie", 90), ("Diana", 62), ("Kent", 30)

for names, scores in students:

	print("student name are : ", names)

	print("student scores are :", scores)
	
	
	if(scores >= 60):
		print(names) 
	
count = 0
	
for student, scores in students:	
	
	if(scores > 50):
	
		count += 1
		
print(count)
		
