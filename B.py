import sys
import math
import itertools as it
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

def hamming(s1,s2):
    #print(s1,s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

if __name__ == "__main__":
    t = [0]*10
    t[0] = 1
    print(t)