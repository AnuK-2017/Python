"""
Find second largest number in array/list
Input: N (number of elements in array)
       array elements separated by space

"""

if __name__ == '__main__':
    n = int(input())
    arr = sorted(set(map(int, input().split())))
    print(arr[-2])