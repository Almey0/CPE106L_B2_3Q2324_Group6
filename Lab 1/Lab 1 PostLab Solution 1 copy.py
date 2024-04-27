'''
Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. 
The median is the number that would appear at the midpoint of a list if it were sorted. The mode is the 
number that appears most frequently in the list. Define these functions in a module named stats.py. Also 
include a function named mean, which computes the average of a set of numbers. Each function expects a list 
of numbers as an argument and returns a single number.
'''

from stats import *

def main():
    input_str = input("Enter a list of numbers separated by spaces: ")
    
    nums = [int(num) for num in input_str.split()]
    
    print("Average:", getAverage(nums))
    print("Median:", getMedian(nums))
    print("Mode:", getMode(nums))

if __name__ == "__main__":
    main()