"""
For Python iMTech Mid Semester Exam - 26 Sep, 2012
For Question 1
newtonRaphson module - must contain a function with the name 'findRealRoots'

"""
# ======================================================================================================


# all your imports, globals and functions come here - between these two separator lines

    
# =======================================================================================================
def p1(x ,roots,polyFn,cRoots):
    p=polyFn(x)
    for root in roots:
        if (root!=x):
            p=p/(x-root)
    for root in cRoots:
        p=p/((x-root)*(x-root.conjugate())).real          
    return p
#def poly(x):
#    polyx = (9*(x**2)+4)*(16*(x**2)+4)*(25*(x**2)+16)*(x-5)*(x+10)*(x-50)*(x-100)*(x+100)
#    return polyx.real
def findRealRoots(polyFn, degree, cRoots, guess, delta, nDigits):
    '''
    Main function called by the tester - calculates the real roots by invoking other functions as necessary
    
    "polyFn" - Function to calculate the value of the polynomial. Just call polyFn(x) for the value at "x"
    "degree" - devity interval to calculate the slope
    "nDigits" - Required computational accuracy in number of significant digits
    '''
    slope=0.0
    rootList = []
    eps=1.0/(10 **nDigits)
    pre=0.0
    # ======================================================================================================
    for i in range (0,degree-2*len(cRoots)):
        pre=guess
        slope=(p1(guess+delta,rootList,polyFn,cRoots)-p1(guess,rootList,polyFn,cRoots))/float(delta)
        x=guess-p1(guess,rootList,polyFn,cRoots)/slope
        while (abs(p1(x,rootList,polyFn,cRoots))>eps and abs(pre-x)>eps):
            slope=(p1(x+delta,rootList,polyFn,cRoots)-p1(x,rootList,polyFn,cRoots))/float(delta)
            prev=x
            x=x-p1(x,rootList,polyFn,cRoots)/slope
        rootList.append(x)
    return rootList
        
        
            
            
        

    # rest of your main code comes here - between these two separator lines

    
    # ======================================================================================================
    return rootList

if __name__ == '__main__':
    print findRealRoots(poly,11,[complex(0,2.0/3.0),complex(0,1.0/2.0),complex(0,4.0/5.0)],25,0.001,5)
    
