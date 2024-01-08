#Question 1:
def reverse_int(num1):

    '''
    Type Contract:
    (int) -> (int)
    
    Description:
    This function will recieve a 3 digit integer(num1) and returns the integers reversed.

    Pre-Conditions:
    num1 must be 3 non-zero integers.
    '''

    #Assigning variables to index coordinates of string.
    a = num1//100
    b = num1//10%10*10
    c = num1%10*100
    
    #Returning reverse index value using concatination.
    return c+b+a
    

#Question 2
def finalMark(labs,assignments,test1,midterm,final):

    '''
    Type Contract:
    (float, float, float, float, float) -> float
    
    Description:
    This function will take 5 float values and return a float of the course final mark.

    Pre-Conditions:
    a,b,c,d,e >0.0 and a,b,c,d,e <100.0.
    '''

    if final > midterm:
        midterm = final
    
    #Finding mark value based on weight
    a = labs*(10/100)
    b = assignments*(20/100)
    c = test1*(10/100)
    d = midterm*(20/100)
    e = final*(40/100)

    #Returing final course mark by adding all previous values
    return float(a+b+c+d+e)


#Question 3
def bibformat(author,title,city,publisher,year):

    '''
    Type Contract:
    (str,str,str,str,int)-> str
    
    Description:
    This function takes the input of 4 strings and 1 integer and returns it to memory in bibliography format.

    Pre-Conditions:
    None
    '''

    #Assigning strings and added needed punctuation to get final result
    Au = author+' '
    Ye = '('+str(year)+')'+'.'
    Ti = ' '+title+'.'
    Ci = ' '+city+':'
    Pu = ' '+publisher+'.'

    #Combining all the strings together
    comb = Au+Ye+Ti+Ci+Pu

    #Returning string of original inputs in bibliography format
    return comb

#Question 4
def bibformatPrint():

    '''
    Type Contract:
    ()-> None
    
    Description:
    This function prompts the user to input the information to make a citation for a book, then calls the function in Q3 and prints parameter values in called funtion.

    Pre-Conditions:
    None
    '''

    #Prompts for user to enter in needed info
    bookt = input("What's the title of this book?: ")
    authnam = input("What's the author's name?: ")
    pubyear = input("What's the year of publication?: ")
    pub = input("What's the publisher's name?: ")
    hq = input("What city is the publisher located in?: ")

    #Assigning results to one variable and calling on function from q3
    result = bibformat(authnam,bookt,hq,pub,pubyear)

    #Printing results of inputted info
    print (result)

#Question 5
def travelTime(kmdist,speedkmh):

    '''
    Type Contract:
    (float,float)-> float
    
    Description:
    This function takes the kilometers traveled and the speed at which the user is going, and finds the time needed to drive that distance in minutes.

    Pre-Conditions:
    kmdist and speedkhm must be the ∈R.
    '''

    #Time taken in hours
    tth = kmdist/speedkmh
    
    #Time taken in minutes
    ttm = tth*60

    return ttm

    
    
    

   
    
