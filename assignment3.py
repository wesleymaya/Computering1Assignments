#Wesley Maya

#Question 1
def triples(chrs):

    '''
    Type Contract:
    (str) -> bool
    
    Description:
    This function takes a string of characters and returns true or false as to if there are 3 consecutive objects in it.

    Pre-Conditions:
    chrs must be a str.
    '''
    

    #Empty acummulator for 3 letters
    acum = ""
    for i in chrs:
        if len(acum) > 2:
            return True

        elif (acum == "") or (i == acum[0]):
            acum = acum + i

        else:
            acum = i
                

    if len(acum) > 2:
        return True

    else:
        return False


        
##        if (acum == "") or (i == acum[0]):
##            acum = acum + i
##
##
##        else:
##            if len(acum) > 2:
##                break
##
##            else:
##                acum = i
##                
##
##    
##    if len(acum) == 3:
##        return True
##
##    else:
##        return False


#Question 2
def countMe(lett):

    '''
    Type Contract:
    (str) -> str
    
    Description:
    This function takes a string and returns a new string with the character, followed by the number of times it is consecutivly repeated in the string (Ex: "aaeee" would be "a2e3").
    
    Pre-Conditions:
    lett must be a str.
    '''

    acum = ""
    cou = ""

    for i in lett:
        if acum == "" or i == acum[0]:
            acum = acum + i

        elif acum[0] != i:
            cou = cou + acum[0] + str(len(acum))
            acum = i

    if acum != "":
        cou = cou + acum[0] + str(len(acum))


    return cou


#Question 3
def sum_odd_divisors(n):

    '''
    Type Contract:
    (int) -> int
    
    Description:
    This function an integer n and returns the sum of all the odd integers of n that divide evenly into n; and then returns this sum as an integer.

    Pre-Conditions:
    n must be an int
    '''

    #Acummulator for postive divisors of n
    posodd = 0

    #What if n is 0
    if n == 0:
        return None

    #Finding if i is odd and divides into n as an integer
    else:
        for i in range(1,abs(n)+1):
            if i%2 != 0 and n%i == 0:
                posodd = posodd + abs(i)

            else:
                None
                    

    #Returns the sum of all odd positve divisors of n
    return posodd


#Question 4
def encrypt(s):

    '''
    Type Contract:
    (str) -> str
    
    Description:
    This function takes a string and encrypts it into a new string where the orginal string is reversed, and then the first and last characters are brought together to become the first and second of the new string, then adding the second and second last to be the third and forth of the new string and so on (Ex: 1234 becomes 4132).

    Pre-Conditions:
    s must be a str
    '''

    revm = s[::-1]
    a = 0
    j = len(revm) -1
    k = j + 1
    newm = ""
    
    #Returning string if 1 object
    if len(s) == 1:
        return s

    else:
        #While the count between letters is greater than 1
        while j >= 1:
            newm += revm[a:k:j]
            a += 1
            k -= 1
            j -= 2

        #Will find if there's a object left in the middle of the string.
        else:
            if len(newm) != len(revm):
                newm += revm[a]

    
    return newm

    

        
