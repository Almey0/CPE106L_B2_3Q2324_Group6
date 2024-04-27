from median import *
from mode import *
import sys

def mean():
    filename = input("Enter the file name: ")
    f = open(filename, 'r')
    
    length = 0
    total = 0
    for line in f:
        num = line.split()
        for index in num:
            total = total + float(index)
            length = length + 1
    
    result = total / length
    
    print("The mean is", result)         

def stats():
    choice = int(input("\nChoose Statistics:\n0: Exit\n1: Mean\n2: Median\n3: Mode\nChoice: "))
    
    match choice:
        case 0:
            print("Exiting...")
            sys.exit()
        case 1:
            mean()
        case 2:
            median()
        case 3:
            mode()
        case _:
            print("Invalid Option\n")
            stats() 