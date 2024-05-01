print("number\tsquare\tcube")
for number in range(6):
    square = number * number
    cube = number * square
    
    print(f"{number:6d}\t{square:6d}\t{cube:4d}\t")

