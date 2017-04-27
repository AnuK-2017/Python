"""
You are given three integers  X, Y, Z  representing the dimensions of a cuboid along with an integer N.
You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to 0.
Here 0<=i<=X, 0<=j<=Y, 0<=k<=Z
"""
if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    multilist = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i+j+k != N]
    print(multilist)