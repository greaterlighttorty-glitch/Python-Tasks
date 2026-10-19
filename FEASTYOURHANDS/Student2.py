products = [("Laptop", 1200), ("Mouse", 25), ("Keyboard", 45), ("Monitor", 300), ("USB Cable", 10)]
def most_expensive_comodities(price):

		if(price[1] > 100):
	
			return price
			
result = filter(most_expensive_comodities, products)

print(tuple(result))




products = [("Laptop", 1200), ("Mouse", 25), ("Keyboard", 45), ("Monitor", 300), ("USB Cable", 10)]

total = 0
for item, price in products:

	total+=price
	
print(total)


products = [("Laptop", 1200), ("Mouse", 25), ("Keyboard", 45), ("Monitor", 300), ("USB Cable", 10)]


for item, price in products: 
	
	print((item) + " price is = ", price)

	print("Laptop price -> ", price(1))


points = [ (2, 3),(-1, 4),(5, -6),(0, 7),(-3, -2)]

def point_checking(points):	
		index, count = points
		return index > 0 and count > 0
		
			
			
result = filter(point_checking, points)

print(tuple(result))


points = [ (2, 3),(-1, 4),(5, -6),(0, 7),(-3, -2)]

for index, count in points:
	
	print(index)
	print(count)

result_one = index.append(count)
new_list = []
result = new_list.append(result_one)

print(result)






employees = [("John", "IT", 50000),("Jane", "HR", 45000),("Mike", "IT", 60000),("Sara", "Finance", 70000)]

for name, department, salary in employees:

	print(name," department is " + department, " and salary is ",  salary)






employees = [("John", "IT", 50000),("Jane", "HR", 45000),("Mike", "IT", 60000),("Sara", "Finance", 70000)]
empty_list = []
for name, department, salary in employees:

	if department == "IT":
		
		empty_list.append(department)
		print(name, " Department is " + department)






employees = [("John", "IT", 50000),("Jane", "HR", 45000),("Mike", "IT", 60000),("Sara", "Finance", 70000)]

for name, department, salary in employees:

	if salary >= 55000:
	
		print ("Employee name is " + name)

