'''
Write a program that allows the user to navigate through the lines of text in a file. 
The program prompts the user for a filename and inputs the lines of text into a list. 
The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. 
Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. 
Otherwise, the program prints the line associated with that number.
'''

def main():
    filename = input("Filename: ")
    
    with open(filename, 'r') as file:
        line = file.readlines()
        
    length = len(line)
    
    while True:
        print("\nThere are", length, "lines in the file")
        number = int(input("Line Number (0 to exit): "))
        
        if number == 0:
            break
        elif 0 < number <= length:
            print(line[number - 1].strip())
        else:
            print("ERROR: Line", number, "does not exist")

if __name__ == '__main__':
    main()