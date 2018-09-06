import math


def quadratic_roots(a,b,c):
 """
    a b and c must produce a real number when used in quadratic program, a b and c can be any type of real number
"""
 print("Equation: " , a,"x^2"," + ", b, "x", " + ", c, " = 0", sep="")
 if(math.pow(b,2) - (4*a*c))> 0:
     print("Two roots.")
     print("x =", (-b + (math.sqrt(math.pow(b,2) - (4*a*c)))) / (2*a))
     print("x =", (-b - (math.sqrt(math.pow(b,2) - (4*a*c)))) / (2*a))
     print("\n")
 elif(math.pow(b,2) - (4*a*c)) < 0:
     print("No roots.")
     print("\n")
 else:
     print("One root.")
     print("x =", -b/(2*a))
     print("\n")

#all test conditions

#conditions that produce 2 roots
quadratic_roots(1,1,0)
quadratic_roots(2,-4,-3)
quadratic_roots(3,10,-25)

#conditions that produce 1 root
quadratic_roots(1,0,0)
quadratic_roots(1,-30,225)
quadratic_roots(25,-30,9)


#conditions that produce no roots
quadratic_roots(1,-5,9)
quadratic_roots(2,-7,12)
quadratic_roots(3,2,15)
