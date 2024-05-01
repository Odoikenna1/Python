#money pyramid
for row in range(6):
    for column in range(row):
        print('$', end=" ")
    print()
    
print()
    
row = 6
column = 0

for i in range(row):
    row-=1
    for i in range(row):
        column+=1
        print('$', end=" ")
    print()