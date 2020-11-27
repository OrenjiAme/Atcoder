import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
        a = [random.randint(0,100) for _ in range(9)]
    
    def f(x):#中央値がx未満である
        if sum(i < x for i in a) < (len(a)-1)/2:
            return True
        return False
    
    left = 0
    right = max(a)
    while right - left > 1:
        mid = (right + left)//2
        if f(mid):
            left = mid
        else:
            right = mid
    a.sort()
    print(a,left,right)#