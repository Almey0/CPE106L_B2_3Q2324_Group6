from median import *
from mode import *

def mean():
    filename = input("Enter the file name: ")
    f = open(filename, 'r')
    
    length = 0
    for line in f:
        num = line.split()
        for index in num:
            total += float(index)
            length = length + 1
    
    result = total / length
    
    print("The mean is", result)         

def stats():
    input = int(print("""
          Choose Statistics:
          0: Exit
          1: Mean
          2: Median
          3: Mode
          """))
    
    match input:
        case 0:
            print()
        case 1:
            mean()
        case 2:
            median()
        case 3:
            mode()
        case _:
            stats() 