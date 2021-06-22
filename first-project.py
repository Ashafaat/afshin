import numpy as np

def poly(x, coefficients):   # value of an arbitrary polynomial function: f(x) = anx^n + an-1x^n-a ... a1x + a0
    value = 0
    degree = len(coefficients) - 1
    for index in range(degree+1):
        value = value + coefficients[index]*(x**(degree - index))
    return value
def dpoly(coefficients):   # derivative of an arbitrary polynomial function: f(x) = anx^n + an-1x^n-a ... a1x + a0
    derivativeCoefficients = []
    degree = len(coefficients) - 1
    for index in range(degree):
        derivativeCoefficients.append(coefficients[index] * (degree - index))
    return derivativeCoefficients

degree = int(input('Enter the degree of your polynomial:\n'))
print('Enter your polynomials as a list of coefficients:')
coefficients = []
for i in range(0, degree+1):
    coefficients.append(int(input()))

roots=set()
semi_roots=set()
for seed in np.arange(-100, 100, 0.1):
    if(len(roots)==degree):
        break
    x0=seed
    for index in range(100):
        derivative_in_x0 = poly(x0, dpoly(coefficients))
        if(derivative_in_x0 != 0):
            x1=x0-(poly(x0, coefficients)/derivative_in_x0)
            if(-0.001<poly(x1, coefficients)<0.001):
                if(poly(round(x1), coefficients)==0):
                    roots.add(round(x1))
                elif(poly(round(x1, 1), coefficients)==0):
                    roots.add(round(x1, 1))
                elif(poly(round(x1, 2), coefficients)==0):
                    roots.add(round(x1, 2))
                elif(poly(round(x1, 3), coefficients)==0):
                    roots.add(round(x1, 3))
                else:
                    semi_roots.add(round(x1, 3))
                break
            else:
                x0=x1
        else:
            break
print('\nNewton\'s method result:\n')
print(len(roots) ,'Exact root(s) found: \n', roots)
print(len(semi_roots) ,'Approximate root(s) found: \n', semi_roots)