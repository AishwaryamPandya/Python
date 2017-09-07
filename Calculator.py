'''
Name: Calculator.py
Description: Simple four operator calculator for whole numbers
Date: September 6 2017
Author: Aishwaryam Pandya
'''
#==============================================================================#

while(1): # while true, keep following the loop running
    print("Calculator") # prints the string inside brackects and quotations  
#==============================================================================#

    num1 = int(input("Num 1 :")) # initialize and request user to input first digit
    num2 = int(input("Num 2 :")) # # initialize and request user to input second digit
    op = input("Enter function operator:") # request user to input operand (+, -, *, /)
#==============================================================================#

    if(op=="+"): # if operand is "+" 
        print(num1+num2) # then add both digits

#==============================================================================#

    elif(op=="-"): # else if operand is "-"
        print(num1-num2) # subtract second digit from first

#==============================================================================#

    elif(op=="*"): # else if operand is "*"
        print(num1*num2) # multiply first digit with second

#==============================================================================#

    elif (op == "/"): # else if operand is "/"
        print(num1/num2) # divide first digit by second

#==============================================================================#    

    else: # else if none of the above
        print("Invalid Operator") # print its invalid operator

#============================== END OF PROGRAM ================================#