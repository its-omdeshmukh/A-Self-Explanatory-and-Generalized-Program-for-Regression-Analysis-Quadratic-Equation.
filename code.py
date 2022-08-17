# Quadratic regression method in Python
# Fitting y = ax^2 + bx + c to given n data points
#Importing Required Libraries
import matplotlib.pyplot as plt
import time
import numpy as np
import sys
 
# Reading value of n
n = int(input("How many data points? "))
 
# Storing  the input values of x and y from user in list
lst1 = [ ]
lst2 = [ ] 
 
# Creating numpy array x & y to store n data points
x = np.zeros(n)
y = np.zeros(n)
 
# Reading data
print("Enter data:")
 
#Taking Input and Storing the data for variables x and y
for i in range(n):
    x[i] = float(input("x["+str(i)+"]= "))
    y[i] = float(input("y["+str(i)+"]= "))
 
# Finding required sum for least square methods
s0, s1, s2, s3, s4, s5, s6 = 0,0,0,0,0,0,0
 
for i in range(n):
    s0 = s0 + x[i]
    s3 = s3 + x[i]*x[i]
    s1 = s1 + y[i]
    s2 = s2 + x[i]*y[i]
    s4 = s4 + x[i]*x[i]*y[i]
    s5 = s5 + x[i]*x[i]*x[i]
    s6 = s6 + x[i]*x[i]*x[i]*x[i]
 
#Creating and Storing the data in matrix as given below
A = [[s3, s0, n  ], [s5, s3, s0 ], [s6, s5, s3 ]]
B = [[s1], [s2], [s4]]
 
# Displaying  the input values of x and y from user in list
lst1.append(x)
lst2.append(y)
print("The data values for Time from users is/are", lst1)
print("The data values for Tensile Strength from users is/are", lst2)
 
#Solving the Matrices to get the values of a, b and c
p = np.linalg.solve(A,B)
print(A)
print(B)
print(p)
print("p[0][0]=", p[0][0])
print("p[1][0]=", p[1][0])
print("p[2][0]=", p[2][0])
a = p[0][0] 
b = p[1][0] 
c = p[2][0]
 
#Displaying the Polynomial Equation of Degree 2/ Quadratic Equation,fitting the Curve from data points
print("And equation is: y = %0.4f x^2 + %0.4f x + %0.4f" %(a,b,c))
 
#Displaying the curve using datapoints from user 
p2 = np.polyfit(x,y,2)
print(p2)
 
#Displaying/ PLotting the curve according to the data points aquired from the user
plt.plot(x,y,'ro',label='Measured (y)')
plt.plot(x,np.polyval(p2,x),'b-',label='Predicted (y)')
plt.legend(); plt.show()
print("End of program")
