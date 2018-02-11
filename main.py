#! /usr/bin/python

from __future__ import division
import matplotlib.pyplot as plt

# j= 0  1  2  3        
X = [1, 3, 4, 6]
Y = [1, 4, 9, 5]
oX = [0, 7]
oY = [0, 25]

def interpolate(X, Y):
    #step 1
    A = Y[:]
    #step 3
    H = []
    for i in range(0, len(X) - 1):
        H.append(X[i+1] -X[i])
    #step 4
    F = []
    F.append((3/H[0])*(A[1]-A[0]))
    for i in range(1, len(A) - 1):
        val = (3/H[i])*(A[i+1]-A[i])-(3/H[i-1])*(A[i]-A[i-1])
        F.append(val)
    #step 5
    L = []
    M = []
    Z = []

    #step 6
    L.append(1)
    M.append(0)
    Z.append(0)

    #step 7

    for i in range(1, len(X)-1):
        val = 2*(X[i+1]-X[i-1])-(H[i-1]*M[i-1])
        L.append(val)
        val = H[i]/L[i]
        M.append(val)
        val = (F[i]-(H[i-1]*Z[i-1]))/L[i]
        Z.append(val)

    #step 8
    L.append(1)
    Z.append(0)

    #my step
    B = []
    C = []
    D = []
    for i in range(0, len(X)):
        B.append(0)
        C.append(0)
        D.append(0)
    #step 9
    for i in reversed(range(0,len(X) -1)):
        C[i] = Z[i] - M[i]*C[i+1]
        B[i] = ((A[i+1] - A[i])/H[i])-(H[i]*(C[i+1]+2*C[i])/3)
        D[i] = (C[i+1]-C[i])/(3*H[i])
    result = []
    for i in range(0, len(X)-1):
        result.append((A[i], B[i], C[i], D[i], X[i]))
    return result



def calculate(x, f):
    a,b,c,d,x0 = f
    return a + b*(x-x0) + c*(x-x0)*(x-x0) + d*(x-x0)*(x-x0)*(x-x0)

def main():
    fn = interpolate(X, Y)
    R = [i/10 for i in range(X[0]*10, X[len(X)-1]*10)]
    V = []
    for i in R:
        for j in range(0, len(X)-1):
            if (i < X[j+1]):
                V.append(calculate(i,fn[j]))
                break

    print(len(R))
    print(len(V))

    draw(X, Y, R, V, oX, oY)




def draw(pointsX, pointsY, X, Y, oX, oY):
    plt.figure(1)
    plt.subplot(311)
    plt.plot(pointsX, pointsY, 'bo')
    plt.axis(oX + oY)

    plt.subplot(312)
    plt.plot(X, Y, 'k')
    plt.axis(oX + oY)

    plt.subplot(313)
    plt.plot(pointsX , pointsY, 'bo', X, Y, 'k')
    plt.axis(oX + oY)

    plt.show()

if __name__ == "__main__":
    main()

