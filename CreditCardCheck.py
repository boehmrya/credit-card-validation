# Ryan Boehm
# CreditCardCheck.py
# CS:1210:0AAA
# HW 08 - Credit Card Check
# Check if a given credit card number (entered by the user) is valid.



# takes a string as an argument, and returns a new string which consists of
# all character at even indices.
def evenChars(string):
    newString = '' #accumulator
    index = 0
    
    # append every other number to a new string
    for i in string:
        if index % 2 == 0:
            newString += string[index]
        index += 1
            
    return newString



# takes a string as an argument, and returns a new string which consists of
# all character at odd indices.
def oddChars(string):
    newString = '' #accumulator
    index = 0
    
    # append every other number to a new string
    for i in string:
        if index % 2 != 0:
            newString += string[index]
        index += 1
            
    return newString



# takes a string of numbers as an argument, doubles each of the numbers, and returns a list of integers.
def doubleNumbers(stringOfNums):
    newList = list(stringOfNums)
    index = 0
    
    # append every other number to a new string
    for item in newList:
        newList[index] = 2 * int(item)
        index += 1
                
    return newList  



# takes a list of integers as an argument, and subtracts n from each integer that is greater than n.
# if an integer is less than or equal to nine, it doesn't change.
def subN(listOfNums, n):
    index = 0
    
    # subtract n from any number greater than nine
    for item in listOfNums:
        if item > 9:
            listOfNums[index] = item - n
        index += 1
    
    return listOfNums



# takes a list of integers as an argument
# returns a list of strings
def intToString(intList):
    strList = []
    for item in intList:
        strList.append(str(item))
    return strList
    


# takes a string of numbers as an argument, returns the sum
def stringSum(string):
    sumTotal = 0 #accumulator for numbers on even indices.
        
    # append every other number to a new string
    for i in string:
        sumTotal += int(i)
            
    return sumTotal 



# takes a string as an argument 
# returns only the digits in a new string (removes all other characters)
def stringNums(string):
    newString = '' #accumulator to compile the numbers
    index = 0
    
    for i in string:
        if string[index].isdigit():
            newString += string[index]
        index += 1
    
    return newString



# takes a number as an argument
# tests whether the number is divisible by 10, returns 'Valid' if so, otherwise returns 'Invalid'
def testValidity(number):
    if number % 10 == 0:
        return 'Valid'
    else:
        return 'Invalid'
    
    
    
# inserts dashes every n characters in a string
# returns a string
def insert_cc_dashes(string, n):
    dashIndices = list(range(n, len(string) + n + 1, n + 1))
    index = 0
    newList = list(string)
    
    for item in newList:
        if index in dashIndices:
            newList.insert(index,'-')
        index += 1
        
    newString = ''.join(newList)
    return newString

    

def creditCardCheck(string):
    stringOfNums = stringNums(string) # strip out any characters that are not digits
    evens = evenChars(stringOfNums) # pull out even characters
    listOfNums = doubleNumbers(evens)  # double each character
    listOfNums = subN(listOfNums, 9)  # subtract nine from each character when necessary
    
    # convert back to a string, compute the sum of even and odd chars
    evens = ''.join(intToString(listOfNums))
    odds = oddChars(stringOfNums)
    evenAndOdd = evens + odds
    sumOfChars = stringSum(evenAndOdd)
    
    # final divisiblity check
    if len(stringOfNums) == 16:
        return testValidity(sumOfChars)
    else:
        return 'Invalid'



def main():
    number = input("Enter a credit card number: ")
    validity = creditCardCheck(number)
    number = insert_cc_dashes(stringNums(number), 4)
    print(number, 'is', validity)
    
    
  
main()            


