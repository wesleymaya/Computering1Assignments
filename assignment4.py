#Wesley Maya

#Assignment 4

#Question 1
def transl(d,s):

    '''
    Type Contract:
    (dict,str) -> str
    
    Description:
    This function takes a dictionary and a string and returns the value of a key or the key of a value corresponding to the string(depending on which it is). If it doesn't exist, it returns the string "Unknown".
    
    Pre-Conditions:
    s must be a string.
    d must be a dictionary.
    '''

    newS = s.lower()

    #Checking if key "s" exists
    if newS in d:
        return d[newS]

    #Else, we are checking if "s" corresponds to a value of a key by iterating through the key values
    else:
        for i in d:
            if newS == d[i]:
                return i

    #Executed if no key or value is found corresponding to "s"
    return "Unknown"


#Adding dict d as a global variable(default dictionary if to use argument d)
d = {"apple":"pomme", "banana":"banane", "pear": "poire", "plum":"prune"}


#Question 2
def setOp(list1, list2):

    '''
    Type Contract:
    (list,list) -> set
    
    Description:
    This function takes two lists and returns a set of the two lists combined.
    
    Pre-Conditions:
    list1 and list2 must be lists.
    '''
    
    #Adding both lists together and manipulating them into a set(set construtor will eliminate mulitple redundant values)
    combset = set(list1 + list2)

    #Returns new set
    return combset
    

#Question 3
def matrixMinMax(m):

    '''
    Type Contract:
    (list) -> tuple
    
    Description:
    This function takes a 2D-list and returns its maximum and minumum values in a tuple.
    
    Pre-Conditions:
    len(m)>0
    '''
    
    #Assigning Max and Min as first numbers
    matmax = m[0][0]
    matmin = m[0][0]

    #For loop starts looking through 2D list for the matrix's minimum and maximum
    for i in m:
        for j in i:
            
            #if j less than current min, replace the min with j
            if j < matmin:
                matmin = j

            #if j more than current max, replace the max with j
            elif j > matmax:
                matmax = j

    #Returning min and max as tuple
    return matmin,matmax


#Question 4
def prodListPos_rec(lst1, leng):

    '''
    Type Contract:
    (list,int) -> int
    
    Description:
    This function takes a list and its length, and returns the product of its positive elements. If the list is empty or contains no numbers > 0, it returns -1.
    
    Pre-Conditions:
    lst1 must be a list.
    leng must be >= 0
    '''

    #Baseline for function
    if leng-1 < 0:
        return 1

    #Recursive returning for positive elements(>0)
    elif lst1[leng-1] >0:
        return prodListPos_rec(lst1, leng-1)*lst1[leng-1]

    #Recursive returning for negative elements(<0)
    else:
        return prodListPos_rec(lst1, leng-1)*1


        
                
