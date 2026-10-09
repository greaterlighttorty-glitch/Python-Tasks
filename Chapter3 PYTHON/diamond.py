symbol = "*"

for index in range(1, 10, 2):

      for space in range(4, (index + 1) // 2 - 1, -1):
            print(" ", end ="")
            
      for count in range(1, index + 1):
            print(symbol, end ="")
            
      print()
      
for index in range(7, 0, -2):

      for space in range(4, (index + 1) // 2 - 1, -1):
            print(" ", end ="")
            
      for count in range(index, 0, -1):
            print(symbol, end ="")
            
      print()
