import statistics

def getAverage(nums):
    return statistics.mean(nums)

def getMedian(nums):
    return statistics.median(nums)

def getMode(nums):
    return statistics.mode(nums)

def main():
    input_str = input("Enter a list of numbers separated by spaces: ")
    
    nums = [int(num) for num in input_str.split()]
    
    print("Average:", getAverage(nums))
    print("Median:", getMedian(nums))
    print("Mode:", getMode(nums))

if __name__ == "__main__":
    main()
