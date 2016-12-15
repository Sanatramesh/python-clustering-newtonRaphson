'''
For Python iMTech Mid Semester Exam - 26 Sep, 2012
For Question 1
Tests newtonRaphson module
'''

import unittest
from testgenDecorator import for_examples
from utils import areListsEqual
from newtonRaphson import findRealRoots

def poly0(x):
    ''' Linear Test Polynomial '''
    return (x-5)

def poly1(x):
    ''' Quadratic Test Polynomial '''
    return (x**2 - 1)

def poly2(x):
    ''' Degree-3 Test Polynomial '''
    return ((9 * x**2) + 25 - (30 * x))

def poly3(x):
    ''' Degree-3 Test Polynomial '''
    return (x-2)*(x-5)*(x-7)

def poly4(x):
    ''' Degree-5 Test Polynomial with a pair of complex roots '''
    cRoot = complex(0, 1)
    polyx = (x-cRoot)*(x-cRoot.conjugate())*(x+3)*(x-2)*(x-1)
    return polyx.real

def poly5(x):
    ''' Degree-6 Test Polynomial with a pair of complex roots '''
    cRoot = complex(1, 2)
    polyx = (x-cRoot)*(x-cRoot.conjugate())*(x-4)*(x-20)*(x+5)*(x+30)
    return polyx.real

def poly6(x):
    ''' Degree-11 Test Polynomial with three pairs of complex roots '''
    polyx = (9*(x**2)+4)*(16*(x**2)+4)*(25*(x**2)+16)*(x-5)*(x+10)*(x-50)*(x-100)*(x+100)
    return polyx.real


class TestNewtonRaphson(unittest.TestCase):
    '''
    Test class for finding the roots of a polynomial
    '''

    nDigits = 5
    roundDigits = nDigits - 2
    delta = 0.001
    
    # ======================================================================================================


    # add any other test cases that you might want to add, here - between these two separator lines


    # =======================================================================================================

    @for_examples((poly0, 1, [], 1, [5]), (poly1, 2, [], 0, [-1, 1]), (poly2, 2, [], 0, [1.667, 1.667]))
    @for_examples((poly3, 3, [], 1, [2, 5, 7]))
    @for_examples((poly4, 5, [complex(0,1)], 0, [-3, 1, 2]))
    @for_examples((poly5, 6, [complex(1,2)], 0, [-30, -5, 4, 20]))
    @for_examples((poly6, 11, [complex(0, (2.0/3.0)), complex(0, (1.0/2.0)), complex(0, (4.0/5.0))], 25, [-100, -10, 5, 50, 100]))
    def testRoots(self, polyFn, degree, cRoots, guess, realRoots):
        '''
        Test finding the roots of the polynomial using Newton-Raphson method
        '''
        r = findRealRoots(polyFn, degree, cRoots, guess, self.delta, self.nDigits)
        r.sort()
        for i, root in enumerate(r):
            r[i] = round(root, self.roundDigits)
        self.assertEqual(True, areListsEqual(realRoots, r))

# --------------------------------------------------
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
