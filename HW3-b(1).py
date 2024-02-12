'''
NON FUNCTIONAL
Not sure which version this is, but
I couldnt make the puzzle pieces fit
'''

def Simpson(fcn, args, a, c, nPoints=1000):

    # Redefine a and b, then calculate the value for h
    a = args[0] - args[1]*5
    b = c
    h = (b-a)/nPoints

    x = list()
    fx = list()
    I = 0
    while I <= nPoints:
        x.append(a+I*h)
        fx.append(fcn(x[I], args))
        I += 1

    result = 0
    I = 0
    while I <= nPoints:
        if I == 0 or I == nPoints:
            result += fx[I]
        elif I % 2 != 0:
            result += 4*fx[I]
        else:
            result += 2*fx[I]
        I += 1
    result = result*(h/3)
    return result

def gamma(alpha):

    #calcs gamma function

def K(df):

    #Calc Km Const using user freedom factor

def Fz(df, z):

    #Calc F(z) given user inputs


def main():
    # Prompt the user to input the degrees of freedom and z value
    df = float(input("Enter the degrees of freedom: "))
    z = float(input("Enter the upper integration limit (z): "))

    # Compute the confidence interval
    interval = compute_confidence_interval(df, z)

    # Output the result
    print(f"Confidence Interval (F(z)) for z ({z}) with {df} degrees of freedom: {interval}")

if __name__ == "__main__":
    main()