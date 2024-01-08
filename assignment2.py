#Wesley Maya

#Question 1
def skate(thickness,temp):

    '''
    Type Contract:
    (float,float) -> (bool)
    
    Description:
    This function receives 2 floats, one of the thickness of the ice, and one of the temperature outside, and returns true or false of whether the canal is open. 

    Pre-Conditions:
    thickness and temp must be real numbers.
    '''

    pos = thickness >=30 and temp <=-10

    return pos


#Question #2
def alphaNote(mark1):

    '''
    Type Contract:
    (float) -> (str)
    
    Description:
    This function takes a float of your mark and returns the letter value.

    Pre-Conditions:
    mark1 >= 0 and mark1 <= 100
    '''
    
    if mark1 >=90 and mark1 <=100:
        letter = "A+"
    elif mark1 >=85 and mark1 <=89:
        letter = "A" 
    elif mark1 >=80 and mark1 <=84:
        letter = "A-"
    elif mark1 >=75 and mark1 <=79:
        letter = "B+"
    elif mark1 >=70 and mark1 <=74:
        letter = "B"
    elif mark1 >=65 and mark1 <=69:
        letter = "C+"
    elif mark1 >=60 and mark1 <=64:
        letter = "C"
    elif mark1 >=55 and mark1 <=59:
        letter = "D+"
    elif mark1 >=50 and mark1 <=54:
        letter = "D"
    elif mark1 >=40 and mark1 <=49:
        letter = "E"
    elif mark1 >=0 and mark1 <=39:
        letter = "F"


    return letter


#Question 3
def alphaNoteVerif():

    '''
    Type Contract:
    () -> None
    
    Description:
    This function asks you to enter your mark, if it is not between 0 and 100(or equal to either number), it will loop the question until it is. After, it will print a message of your letter and print another below of whether you passed or failed.

    Pre-Conditions:
    None
    '''

    m = float(input("What is your mark?: "))
    

    if m >= 0 and m <= 100:
        result = alphaNote(m)
        print("The letter you got is:",result)
        if m <=49:
            print("Failed")
        else:
            print("Passed")
    else:
        return alphaNoteVerif()


#Question 4
def loops(n):

    '''
    Type Contract:
    (int) -> None
    
    Description:
    This function will recieve an integer and print every second value of it from 1 to n on one line, and then, will print every value from n to 1 on the next.

    Pre-Conditions:
    n must be an int.
    '''
    
    for p in range(1,n+1,2):
        print(p, end=" ")

    print()

    for k in range(-n,0,2):
        print(-k, end=" ")



#Question 5
def test_password(pw):

    '''
    Type Contract:
    (str) -> (bool)
    
    Description:
    This function takes a string of a password and checks to see if it meets all the requirements of the system.

    Pre-Conditions:
    pw must be a str. 
    '''
    #Counter for upper case letters
    capup = ""
    #Counter for lower case letters
    caplow = ""
    #Counter for numbers
    nums = ""
    #Counter for special characters
    spec = ""


    for i in pw:
        if ord(i) in range(65,91):
            capup = capup + i
        elif ord(i) in range(97,123):
            caplow = caplow + i
        elif ord(i) in range(48,58):
            nums = nums + i
        elif i in "@-#$%":
            spec = spec + i
        else:
            None

    else:
        if len(capup + caplow + nums + spec) != len(pw):
            return False

        else:
            if (len(pw) >= 8 and len(pw) <= 16) == False:
               return False

            else:
                if len(capup) >=1 and len(caplow) >= 1 and len(nums) >= 1 and len(spec) >= 1:
                    return True
                
                else:
                    return False
    



def tester():

    '''
    Type Contract:
    () -> (str)
    
    Description:
    This function prompts the user to enter in a password they would like to use and calls on test_password() to check the requirements.
    
    Pre-Conditions:
    None. 
    '''

    #Prompted question to user
    ask = input("What is your password?: ")

    #bool result from test_password() function
    result = test_password(ask)

    if result == True:
        print("Great, this password meets all the requirments!")

    else:
        print("This password does not meet all the requirements, try again")

        

    


        
        
        
     
        
        
        
    
    
