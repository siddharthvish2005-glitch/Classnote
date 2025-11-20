rows = int(input("Enter the number of rows for Pascal's Triangle: "))


row_list = [1]
print(row_list[0])


for i in range(1, rows):
  
    next_row = [1]
    for j in range(1, i):
       
        next_row.append(row_list[j-1] + row_list[j])
    next_row.append(1)
    
   
    print(" ".join(map(str, next_row)))
    
   
    row_list = next_row